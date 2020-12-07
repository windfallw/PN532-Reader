from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt5.QtGui import QIcon
from SLmge import *
from rfid import *
import sys


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionOpenFile.triggered.connect(self.openFile)
        self.openSerial.clicked.connect()
        # self.show_port_list()

    # def show_port_list(self):
    #     for dev in getSerial():
    #         print(dev.device, dev.description)
    #         self.allSerialPort.addItem(dev.description)

    def openFile(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files( *);;Text Files(*.txt)")
        self.statusbar.showMessage(file)


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("./icon.svg"))
win = MyMainWindow()
win.show()
sys.exit(app.exec_())
