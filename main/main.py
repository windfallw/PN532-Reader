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
        self.work.trigger_byte.connect(self.printByte)
        self.work.trigger_str.connect(self.printStr)

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


class WorkThread(QThread):
    trigger_byte = pyqtSignal(bytes)
    trigger_str = pyqtSignal(str)

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
                    self.trigger_byte.emit(res[13:-2])

            time.sleep(0.005)


device = RFID_YES()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
