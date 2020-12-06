from PyQt5 import QtWidgets, QtCore
import SLmge
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindows = QtWidgets.QMainWindow()
ui = SLmge.Ui_MainWindow()
ui.setupUi(MainWindows)
MainWindows.show()
sys.exit(app.exec_())
