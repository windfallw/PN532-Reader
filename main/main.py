from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QIcon, QTextCursor
from src.SLmge import *
from rfid import RFID_YES, time
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.refreshPORTList()
        self.port.currentIndexChanged.connect(self.changeSER)

        self.refreshBDList()
        self.baud.currentIndexChanged.connect(self.changeBR)

        self.openSer.clicked.connect(self.openSER)

        self.read125k.setAutoRepeat(False)
        self.read125k.clicked.connect(self.find125k)

        self.read14443.setAutoRepeat(False)
        self.read14443.clicked.connect(self.find14443)

    def refreshBDList(self):
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
            work.start()
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


class WorkThread(QThread):
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
                content = data.decode("utf-8", "replace")
                win.serialPrint.moveCursor(QTextCursor.End)
                win.serialPrint.insertPlainText(content)
                # print(content, end='')
                # decode ignore or replace
            time.sleep(0.005)


device = RFID_YES()
work = WorkThread()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./src/icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
