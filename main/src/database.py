# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_showData(object):
    def setupUi(self, showData):
        showData.setObjectName("showData")
        showData.resize(543, 392)
        self.gridLayout_2 = QtWidgets.QGridLayout(showData)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tableDialog_false = QtWidgets.QPushButton(showData)
        self.tableDialog_false.setObjectName("tableDialog_false")
        self.gridLayout.addWidget(self.tableDialog_false, 1, 1, 1, 1)
        self.tableDialog_true = QtWidgets.QPushButton(showData)
        self.tableDialog_true.setObjectName("tableDialog_true")
        self.gridLayout.addWidget(self.tableDialog_true, 1, 0, 1, 1)
        self.dataTable = QtWidgets.QTableWidget(showData)
        self.dataTable.setObjectName("dataTable")
        self.dataTable.setColumnCount(5)
        self.dataTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataTable.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.dataTable, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(showData)
        QtCore.QMetaObject.connectSlotsByName(showData)

    def retranslateUi(self, showData):
        _translate = QtCore.QCoreApplication.translate
        showData.setWindowTitle(_translate("showData", "Form"))
        self.tableDialog_false.setText(_translate("showData", "取消"))
        self.tableDialog_true.setText(_translate("showData", "确定"))
        item = self.dataTable.horizontalHeaderItem(0)
        item.setText(_translate("showData", "卡号"))
        item = self.dataTable.horizontalHeaderItem(1)
        item.setText(_translate("showData", "姓名"))
        item = self.dataTable.horizontalHeaderItem(2)
        item.setText(_translate("showData", "学号"))
        item = self.dataTable.horizontalHeaderItem(3)
        item.setText(_translate("showData", "性别"))
        item = self.dataTable.horizontalHeaderItem(4)
        item.setText(_translate("showData", "专业"))
