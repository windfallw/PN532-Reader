from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
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

        self.refreshPORTList()
        self.refreshBDList()

        # self.work.trigger125.connect()
        # self.work.trigger14443.connect()

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

    def throwErr(self, func, err=None):
        try:
            func()
        except Exception as e:
            if err:
                QMessageBox.critical(self, '错误', err)
            else:
                QMessageBox.critical(self, '错误', str(e))


class WorkThread(QThread):
    trigger125 = pyqtSignal(bytes)
    trigger14443 = pyqtSignal(bytes)

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
                content = data.decode("utf-8", "replace")  # ignore or replace
                win.serialPrint.moveCursor(QTextCursor.End)
                win.serialPrint.insertPlainText(content)
                self.trigger125.emit(data)
                self.trigger14443.emit(data)
                # print(content, end='')
            time.sleep(0.005)


device = RFID_YES()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
