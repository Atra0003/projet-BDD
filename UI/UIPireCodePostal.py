# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PireCodePostal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PireCodePostal(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 895)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/Images/DesignBgr.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 160, 391, 451))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.widget.setFont(font)
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.labelCheckOpinion = QtWidgets.QLabel(self.widget)
        self.labelCheckOpinion.setGeometry(QtCore.QRect(0, 10, 391, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        self.labelCheckOpinion.setFont(font)
        self.labelCheckOpinion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCheckOpinion.setObjectName("labelCheckOpinion")
        self.listWidgetCodePostalObtenu = QtWidgets.QListWidget(self.widget)
        self.listWidgetCodePostalObtenu.setGeometry(QtCore.QRect(40, 70, 311, 311))
        self.listWidgetCodePostalObtenu.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:6px;")
        self.listWidgetCodePostalObtenu.setObjectName("listWidgetCodePostalObtenu")
        self.buttonBoxOkRetour = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour.setGeometry(QtCore.QRect(250, 580, 171, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.buttonBoxOkRetour.setFont(font)
        self.buttonBoxOkRetour.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOkRetour.setCenterButtons(True)
        self.buttonBoxOkRetour.setObjectName("buttonBoxOkRetour")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelCheckOpinion.setText(_translate("MainWindow", "Code postal avec les - restaurants"))
from . import res_rc
