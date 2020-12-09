from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QIcon
from SLmge import *
from rfid import *
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        self.port.addItems(f14443.dev_list)
        f14443.ser.port = self.port.currentText()
        self.port.currentIndexChanged.connect(self.changeSER)

        self.baud.addItems(f14443.bd_list)
        self.baud.setCurrentIndex(2)
        f14443.ser.baudrate = int(self.baud.currentText())
        self.baud.currentIndexChanged.connect(self.changeBR)

        self.openSer.clicked.connect(self.openSER)

    def changeSER(self):
        f14443.ser.port = self.port.currentText()
        print(f14443.ser.port)

    def changeBR(self):
        f14443.ser.baudrate = int(self.baud.currentText())
        print(f14443.ser.baudrate)

    def openSER(self):
        self.openSer.setEnabled(False)
        f14443.open()
        # work.start()
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
        f14443.open()


f14443 = RFID_YES()
work = WorkThread()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./icon.svg"))

win = MyMainWindow()
win.show()

sys.exit(app.exec_())
