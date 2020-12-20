from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QTextCursor
from rfid import RFID_YES, time
from src.SLmge import *
from sql import *
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.work = WorkThread()
        self.work.trigger.connect(self.whichCard)

        self.refreshPORTList()
        self.refreshBDList()

        self.port.currentIndexChanged.connect(self.changeSER)
        self.baud.currentIndexChanged.connect(self.changeBR)
        self.openSer.clicked.connect(self.openSER)
        self.read125k.clicked.connect(self.find125k)
        self.read14443.clicked.connect(self.find14443)

    def refreshBDList(self):
        if not device.ser.isOpen():
            self.baud.clear()
            self.baud.addItems(device.bd_list)
            self.baud.setCurrentIndex(2)
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
            device.HF14443()
        else:
            QMessageBox.information(self, '提示', '请先打开串口')

    def whichCard(self, data):
        # try:
        if data.startswith(b'C\xbc\x12\x01\x02\n\x86\x00\x01') and len(data) == 18:
            cardID = data[10:14].hex()
            self.serialPrint.moveCursor(QTextCursor.End)
            self.serialPrint.append(str(cardID))
            if findSQL(cardID):
                QMessageBox.information(self, '125k只读卡', '卡号: %s' % cardID)
            else:
                QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：')

        elif data.startswith(b'C\xbc\x0c\x02') and len(data) == 12:
            cardID = data[6:10].hex()
            self.serialPrint.moveCursor(QTextCursor.End)
            self.serialPrint.append(str(cardID))
            if findSQL(cardID):
                QMessageBox.information(self, 'HF14443卡', '卡号: %s' % cardID)
            else:
                QInputDialog.getText(self, 'Text Input Dialog', '输入姓名：')

        elif data.startswith(b'C\xbc\x12\x01\x02\n\x86\x14\x01') and len(data) == 18:
            QMessageBox.critical(self, '错误', '125k只读卡读卡失败')

        else:
            pass
        # except Exception as e:
        #     print(e)


class WorkThread(QThread):
    trigger = pyqtSignal(bytes)

    def __init__(self, parent=None):
        super(WorkThread, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while True:
            data = device.ser.readall()
            if data != b'':
                # content = data.decode("utf-8", "replace")  # ignore or replace
                # print(content, end='')
                # win.serialPrint.insertPlainText(content)
                win.serialPrint.moveCursor(QTextCursor.End)
                win.serialPrint.append(str(data))
                self.trigger.emit(data)
            time.sleep(0.005)


device = RFID_YES()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
