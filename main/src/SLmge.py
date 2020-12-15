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
        MainWindow.resize(644, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 0, 0, 1, 1)
        self.baud_label = QtWidgets.QLabel(self.centralwidget)
        self.baud_label.setObjectName("baud_label")
        self.gridLayout.addWidget(self.baud_label, 0, 1, 1, 1)
        self.port = QtWidgets.QComboBox(self.centralwidget)
        self.port.setEditable(False)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 0, 1, 1)
        self.baud = QtWidgets.QComboBox(self.centralwidget)
        self.baud.setObjectName("baud")
        self.gridLayout.addWidget(self.baud, 1, 1, 1, 1)
        self.openSer = QtWidgets.QPushButton(self.centralwidget)
        self.openSer.setObjectName("openSer")
        self.gridLayout.addWidget(self.openSer, 1, 2, 1, 1)
        self.read125k = QtWidgets.QPushButton(self.centralwidget)
        self.read125k.setObjectName("read125k")
        self.gridLayout.addWidget(self.read125k, 1, 3, 1, 1)
        self.read14443 = QtWidgets.QPushButton(self.centralwidget)
        self.read14443.setObjectName("read14443")
        self.gridLayout.addWidget(self.read14443, 1, 4, 1, 1)
        self.showSql = QtWidgets.QPushButton(self.centralwidget)
        self.showSql.setObjectName("showSql")
        self.gridLayout.addWidget(self.showSql, 1, 5, 1, 1)
        self.serialPrint = QtWidgets.QTextBrowser(self.centralwidget)
        self.serialPrint.setObjectName("serialPrint")
        self.gridLayout.addWidget(self.serialPrint, 2, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 644, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.menu.addAction(self.actionabout)
        self.menuBar.addAction(self.menu.menuAction())
        self.port_label.setBuddy(self.port)
        self.baud_label.setBuddy(self.baud)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.port, self.baud)
        MainWindow.setTabOrder(self.baud, self.openSer)
        MainWindow.setTabOrder(self.openSer, self.read125k)
        MainWindow.setTabOrder(self.read125k, self.read14443)
        MainWindow.setTabOrder(self.read14443, self.showSql)
        MainWindow.setTabOrder(self.showSql, self.serialPrint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.port_label.setText(_translate("MainWindow", "串口"))
        self.baud_label.setText(_translate("MainWindow", "波特率"))
        self.openSer.setText(_translate("MainWindow", "打开"))
        self.read125k.setText(_translate("MainWindow", "125K只读卡"))
        self.read14443.setText(_translate("MainWindow", "HF14443读卡"))
        self.showSql.setText(_translate("MainWindow", "查看数据库"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionabout.setText(_translate("MainWindow", "关于"))