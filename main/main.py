from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication
from PyQt5.QtGui import QIcon, QTextCursor

from src.SLmge import *
from src.dialog import *
from src.database import *

from rfid import RFID, time
from sql import *

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

        self.refreshPORTList()
        self.refreshBDList()

        self.port.currentIndexChanged.connect(self.changeSER)
        self.baud.currentIndexChanged.connect(self.changeBR)
        self.openSer.clicked.connect(self.openSER)
        self.read125k.clicked.connect(self.find125k)
        self.read14443.clicked.connect(self.find14443)
        self.showSql.clicked.connect(self.showSQL)

    def refreshBDList(self):
        if not device.ser.isOpen():
            self.baud.clear()
            self.baud.addItems(device.bd_list)
            self.baud.setCurrentIndex(6)
            device.ser.baudrate = int(self.baud.currentText())

    def refreshPORTList(self):
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
        if device.open():
            self.openSer.setEnabled(False)
            self.work.start()
        else:
            QMessageBox.critical(self, '错误', '打开串口失败')
        # self.openSer.setCheckable(True)
        # print(self.openSer.isChecked())

    def find125k(self):
        if device.ser.isOpen():
            device.readOnlyCard()
        else:
            QMessageBox.information(self, '提示', '请先打开串口')

    def find14443(self):
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

    def showSQL(self):
        database.refresh()
        database.show()


class WorkThread(QThread):
    trigger_byte = pyqtSignal(bytes)
    trigger_str = pyqtSignal(str)
    trigger_find = pyqtSignal(str)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        device.pn532WakeUp()
        if device.ser.readall() == device.pn532_res_wake:
            self.trigger_str.emit('wake up PN532 successfully .')
        while True:
            data = device.ser.readall()
            if data.startswith(b'\x00\x00\xff\x00\xff\x00') and len(data) > 6:
                res = data.replace(b'\x00\x00\xff\x00\xff\x00', b'')
                self.trigger_byte.emit(res)
                if res.startswith(b'\x00\x00\xff\x0c\xf4\xd5K\x01\x01\x00\x04\x08\x04') and res.endswith(b'\x00'):
                    cardID = res[13:-2].hex().upper()
                    self.trigger_find.emit(str(cardID))

            time.sleep(0.005)


device = RFID()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))

dialog = Dialog()
database = Database()

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
