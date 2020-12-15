from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QIcon, QTextCursor
from src.SLmge import *
from rfid import RFID_YES, time
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.port.addItems(device.dev_list)
        device.ser.port = self.port.currentText()
        self.port.currentIndexChanged.connect(self.changeSER)

        self.baud.addItems(device.bd_list)
        self.baud.setCurrentIndex(2)
        device.ser.baudrate = int(self.baud.currentText())
        self.baud.currentIndexChanged.connect(self.changeBR)

        self.openSer.clicked.connect(self.openSER)

        self.read125k.setAutoRepeat(False)
        self.read125k.clicked.connect(self.find125k)

        self.read14443.setAutoRepeat(False)
        self.read14443.clicked.connect(self.find14443)

    def changeSER(self):
        device.ser.port = self.port.currentText()
        print(device.ser.port)

    def changeBR(self):
        device.ser.baudrate = int(self.baud.currentText())
        print(device.ser.baudrate)

    def openSER(self):
        self.openSer.setEnabled(False)
        device.open()
        work.start()
        # self.openSer.setCheckable(True)
        # print(self.openSer.isChecked())

    def find125k(self):
        device.readOnlyCard()

    def find14443(self):
        device.HF14443()


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
