# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SLmge.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.read14443 = QtWidgets.QPushButton(self.centralwidget)
        self.read14443.setObjectName("read14443")
        self.gridLayout.addWidget(self.read14443, 2, 4, 1, 1)
        self.showSQL = QtWidgets.QPushButton(self.centralwidget)
        self.showSQL.setObjectName("showSQL")
        self.gridLayout.addWidget(self.showSQL, 2, 5, 1, 1)
        self.port = QtWidgets.QComboBox(self.centralwidget)
        self.port.setEditable(False)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 2, 0, 1, 1)
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 0, 0, 1, 1)
        self.wakeUP = QtWidgets.QPushButton(self.centralwidget)
        self.wakeUP.setObjectName("wakeUP")
        self.gridLayout.addWidget(self.wakeUP, 2, 3, 1, 1)
        self.baud_label = QtWidgets.QLabel(self.centralwidget)
        self.baud_label.setObjectName("baud_label")
        self.gridLayout.addWidget(self.baud_label, 0, 1, 1, 1)
        self.openSer = QtWidgets.QPushButton(self.centralwidget)
        self.openSer.setObjectName("openSer")
        self.gridLayout.addWidget(self.openSer, 2, 2, 1, 1)
        self.serialPrint = QtWidgets.QTextBrowser(self.centralwidget)
        self.serialPrint.setObjectName("serialPrint")
        self.gridLayout.addWidget(self.serialPrint, 3, 0, 1, 6)
        self.baud = QtWidgets.QComboBox(self.centralwidget)
        self.baud.setObjectName("baud")
        self.gridLayout.addWidget(self.baud, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 605, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSQL = QtWidgets.QAction(MainWindow)
        self.actionSQL.setObjectName("actionSQL")
        self.menu.addAction(self.actionAbout)
        self.menu.addAction(self.actionSQL)
        self.menuBar.addAction(self.menu.menuAction())
        self.port_label.setBuddy(self.port)
        self.baud_label.setBuddy(self.baud)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.port, self.openSer)
        MainWindow.setTabOrder(self.openSer, self.wakeUP)
        MainWindow.setTabOrder(self.wakeUP, self.read14443)
        MainWindow.setTabOrder(self.read14443, self.showSQL)
        MainWindow.setTabOrder(self.showSQL, self.serialPrint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主程序"))
        self.read14443.setText(_translate("MainWindow", "读卡"))
        self.showSQL.setText(_translate("MainWindow", "查看数据库"))
        self.port_label.setText(_translate("MainWindow", "串口"))
        self.wakeUP.setText(_translate("MainWindow", "唤醒"))
        self.baud_label.setText(_translate("MainWindow", "波特率"))
        self.openSer.setText(_translate("MainWindow", "打开"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionSQL.setText(_translate("MainWindow", "查看数据库"))
