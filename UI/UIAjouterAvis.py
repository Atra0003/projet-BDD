# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientAddOpinion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AjouterAvis(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 900)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/Images/DesignBgr.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 160, 391, 451))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.widget.setFont(font)
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.labelAddAvis = QtWidgets.QLabel(self.widget)
        self.labelAddAvis.setGeometry(QtCore.QRect(80, 0, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.labelAddAvis.setFont(font)
        self.labelAddAvis.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAddAvis.setObjectName("labelAddAvis")
        self.lineEditRestoName = QtWidgets.QLineEdit(self.widget)
        self.lineEditRestoName.setGeometry(QtCore.QRect(80, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEditRestoName.setFont(font)
        self.lineEditRestoName.setTabletTracking(False)
        self.lineEditRestoName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineEditRestoName.setObjectName("lineEditRestoName")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(80, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.dateEdit.setObjectName("dateEdit")
        self.labelVisite = QtWidgets.QLabel(self.widget)
        self.labelVisite.setGeometry(QtCore.QRect(80, 90, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelVisite.setFont(font)
        self.labelVisite.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelVisite.setObjectName("labelVisite")
        self.timeEditHeureDebut = QtWidgets.QTimeEdit(self.widget)
        self.timeEditHeureDebut.setGeometry(QtCore.QRect(80, 190, 101, 31))
        self.timeEditHeureDebut.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.timeEditHeureDebut.setObjectName("timeEditHeureDebut")
        self.timeEditHeureFin = QtWidgets.QTimeEdit(self.widget)
        self.timeEditHeureFin.setGeometry(QtCore.QRect(227, 190, 101, 31))
        self.timeEditHeureFin.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.timeEditHeureFin.setObjectName("timeEditHeureFin")
        self.labelVisite2 = QtWidgets.QLabel(self.widget)
        self.labelVisite2.setGeometry(QtCore.QRect(190, 199, 21, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelVisite2.setFont(font)
        self.labelVisite2.setStyleSheet("")
        self.labelVisite2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVisite2.setObjectName("labelVisite2")
        self.plainTextEditPlatCommande = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEditPlatCommande.setGeometry(QtCore.QRect(30, 240, 351, 111))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.plainTextEditPlatCommande.setFont(font)
        self.plainTextEditPlatCommande.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.plainTextEditPlatCommande.setDocumentTitle("")
        self.plainTextEditPlatCommande.setObjectName("plainTextEditPlatCommande")
        self.lineEditPrixPaye = QtWidgets.QLineEdit(self.widget)
        self.lineEditPrixPaye.setGeometry(QtCore.QRect(80, 360, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEditPrixPaye.setFont(font)
        self.lineEditPrixPaye.setTabletTracking(False)
        self.lineEditPrixPaye.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineEditPrixPaye.setObjectName("lineEditPrixPaye")
        self.labelError = QtWidgets.QLabel(self.widget)
        self.labelError.setGeometry(QtCore.QRect(-90, 400, 600, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setText("")
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.buttonBoxOkRetour = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour.setGeometry(QtCore.QRect(250, 590, 171, 16))
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
        self.labelAddAvis.setText(_translate("MainWindow", "Ajouter un Avis"))
        self.lineEditRestoName.setText(_translate("MainWindow", "Nom du Restaurant"))
        self.labelVisite.setText(_translate("MainWindow", "Date et Heure de Visite"))
        self.labelVisite2.setText(_translate("MainWindow", "-"))
        self.plainTextEditPlatCommande.setPlainText(_translate("MainWindow", "Lister les Plat commandes"))
        self.lineEditPrixPaye.setText(_translate("MainWindow", "Prix Total paye"))
from . import res_rc
