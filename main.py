from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QIcon, QTextCursor
from SLmge import *
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
        self.read125k.clicked.connect()

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
            data = device.ser.readline()
            if data != b'':
                content = data.decode("utf-8", "replace")
                win.serialPrint.insertPlainText(content)
                win.serialPrint.moveCursor(QTextCursor.End)
                # print(content, end='')
                # decode ignore or replace
                time.sleep(0.001)


device = RFID_YES()
work = WorkThread()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
