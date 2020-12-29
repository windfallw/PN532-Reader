from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QTextCursor

from src.SLmge import *
from src.dialog import *
from src.database import *

from rfid import RFID
from sql import *

import time
import sys


class Dialog(QDialog, Ui_addUser):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setModal(True)
        self.setupUi(self)
        self.dialog_true.clicked.connect(self.click_true)
        self.dialog_false.clicked.connect(self.close)

    def click_true(self):
        if self.userName.text() and self.userNumber.text() and self.major.text() != '':
            ID = self.CardID.text()
            name = self.userName.text()
            number = self.userNumber.text()
            sex = self.sex.currentText()
            major = self.major.text()
            result = insertSQL(ID, name, number, sex, major)
            if result:
                QMessageBox.critical(self, '错误', str(result))
                return
            QMessageBox.information(self, '提示', '插入成功')
            self.close()
        else:
            QMessageBox.critical(self, '错误', '每一个字段都不能为空！')


class Database(QTableWidget, Ui_showData):
    def __init__(self, parent=None):
        super(QTableWidget, self).__init__(parent)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) 窗口置顶
        self.setupUi(self)
        self.tableDialog_true.clicked.connect(self.click_true)
        self.tableDialog_false.clicked.connect(self.close)
        self.delData.clicked.connect(self.removeData)

    def removeData(self):
        items = getIdSQL()
        select = QInputDialog.getItem(self, "删除记录", '卡号', items, 0, False)
        result = removeSQL(select[0])
        if result:
            QMessageBox.critical(self, '错误', str(result))
        else:
            QMessageBox.information(self, '提示', '删除卡号: %s 成功' % select[0])
            self.refresh()

    def refresh(self):
        data = getSQL()
        self.dataTable.clearContents()
        self.dataTable.setRowCount(0)
        for row, items in enumerate(data):
            self.dataTable.insertRow(row)
            for col, item in enumerate(items):
                self.dataTable.setItem(row, col, QTableWidgetItem(item))

    def click_true(self):
        rows = self.dataTable.rowCount()
        cols = self.dataTable.columnCount()
        for row in range(rows):
            rowData = []
            for col in range(cols):
                rowData.append(self.dataTable.item(row, col).text())
            result = updateSQL(*rowData)
            if result:
                QMessageBox.critical(self, '错误', str(result))
                return
        self.refresh()
        QMessageBox.information(self, '提示', '所有数据已更新')


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.work = WorkThread()
        self.work.trigger_byte.connect(self.printByte)
        self.work.trigger_str.connect(self.printStr)
        self.work.trigger_find.connect(self.showMsg)
        self.work.trigger_err.connect(self.Error)

        self.refreshPORTList()
        self.refreshBDList()

        self.port.currentIndexChanged.connect(self.changeSER)
        self.port.popupAboutToBeShown.connect(self.refreshPORTList)

        self.baud.currentIndexChanged.connect(self.changeBR)
        self.openSer.clicked.connect(self.openSER)
        self.wakeUP.clicked.connect(self.wakePN532)
        self.readCard.clicked.connect(self.findCard)
        self.showSQL.clicked.connect(self.showSQLData)
        self.actionSQL.triggered.connect(self.showSQLData)

    def refreshBDList(self):
        if not device.ser.isOpen():
            self.baud.clear()
            self.baud.addItems(device.bd_list)
            self.baud.setCurrentIndex(6)
            device.ser.baudrate = int(self.baud.currentText())

    def refreshPORTList(self):
        device.getSerial()
        self.port.clear()
        self.port.addItems(device.dev_list)
        device.ser.port = self.port.currentText()

    def changeSER(self):
        device.ser.port = self.port.currentText()
        print(device.ser.port)

    def changeBR(self):
        device.ser.baudrate = int(self.baud.currentText())
        print(device.ser.baudrate)

    def openSER(self):
        if device.ser.isOpen():
            self.work.stop()
            device.close()
            self.openSer.setText('打开')
        else:
            errmsg = device.open()
            if errmsg:
                QMessageBox.critical(self, '错误', str(errmsg))
            else:
                self.work.start()
                self.openSer.setText('关闭')

    def wakePN532(self):
        if device.ser.isOpen():
            device.pn532WakeUp()
        else:
            QMessageBox.information(self, '提示', '请先打开串口')

    def findCard(self):
        if device.ser.isOpen():
            device.pn532find()
        else:
            QMessageBox.information(self, '提示', '请先打开串口')

    def printByte(self, data):
        self.serialPrint.moveCursor(QTextCursor.End)
        # self.serialPrint.append(str(data))
        self.serialPrint.append(data.hex(' '))

    def printStr(self, data):
        self.serialPrint.moveCursor(QTextCursor.End)
        self.serialPrint.append(data)

    def showMsg(self, msg):
        result = findSQL(msg)
        if findSQL(msg):
            searchResult = '卡号: {}\n姓名: {}\n学号: {}\n性别: {}\n专业: {}'.format(*result)
            QMessageBox.information(self, '已登记', searchResult)
        else:
            dialog.CardID.setText(msg)
            dialog.show()

    def showSQLData(self):
        database.refresh()
        database.show()

    def Error(self, msg):
        QMessageBox.critical(self, '错误', str(msg))
        device.close()
        self.openSer.setText('打开')


class WorkThread(QThread):
    trigger_byte = pyqtSignal(bytes)
    trigger_str = pyqtSignal(str)
    trigger_find = pyqtSignal(str)
    trigger_err = pyqtSignal(str)
    working = False

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)

    def __del__(self):
        self.stop()

    def stop(self):
        self.working = False
        self.wait()

    def run(self):
        self.working = True
        device.pn532WakeUp()
        while self.working:
            try:
                data = device.ser.readall()
                if data.startswith(b'\x00\x00\xff\x00\xff\x00') and len(data) > 6:
                    res = data.replace(b'\x00\x00\xff\x00\xff\x00', b'')
                    self.trigger_byte.emit(res)
                    if res.startswith(b'\x00\x00\xff\x0c\xf4\xd5K\x01\x01\x00\x04\x08\x04') and res.endswith(b'\x00'):
                        cardID = res[13:-2].hex().upper()
                        self.trigger_find.emit(str(cardID))
                    elif res == device.pn532_res_wake:
                        self.trigger_str.emit('wake up PN532 successfully .')
                time.sleep(0.005)
            except Exception as err:
                self.trigger_err.emit(str(err))
                self.stop()


device = RFID()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))

dialog = Dialog()
database = Database()

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
