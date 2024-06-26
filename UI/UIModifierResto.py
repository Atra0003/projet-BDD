# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RestaurateurEditResto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifierResto(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 900)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/Images/DesignBgr.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(140, 160, 391, 451))
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.labelEditResto = QtWidgets.QLabel(self.widget)
        self.labelEditResto.setGeometry(QtCore.QRect(10, 10, 421, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.labelEditResto.setFont(font)
        self.labelEditResto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEditResto.setObjectName("labelEditResto")
        self.lineRestoName = QtWidgets.QLineEdit(self.widget)
        self.lineRestoName.setGeometry(QtCore.QRect(90, 50, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineRestoName.setFont(font)
        self.lineRestoName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineRestoName.setObjectName("lineRestoName")
        self.lineTypeNourriture = QtWidgets.QLineEdit(self.widget)
        self.lineTypeNourriture.setGeometry(QtCore.QRect(90, 220, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineTypeNourriture.setFont(font)
        self.lineTypeNourriture.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineTypeNourriture.setObjectName("lineTypeNourriture")
        self.lineAdRue = QtWidgets.QLineEdit(self.widget)
        self.lineAdRue.setGeometry(QtCore.QRect(90, 90, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineAdRue.setFont(font)
        self.lineAdRue.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineAdRue.setObjectName("lineAdRue")
        self.lineAdVille = QtWidgets.QLineEdit(self.widget)
        self.lineAdVille.setGeometry(QtCore.QRect(90, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineAdVille.setFont(font)
        self.lineAdVille.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineAdVille.setObjectName("lineAdVille")
        self.lineAdPostal = QtWidgets.QLineEdit(self.widget)
        self.lineAdPostal.setGeometry(QtCore.QRect(90, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineAdPostal.setFont(font)
        self.lineAdPostal.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineAdPostal.setObjectName("lineAdPostal")
        self.lineAdNum = QtWidgets.QLineEdit(self.widget)
        self.lineAdNum.setGeometry(QtCore.QRect(230, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineAdNum.setFont(font)
        self.lineAdNum.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineAdNum.setObjectName("lineAdNum")
        self.lineCountry = QtWidgets.QLineEdit(self.widget)
        self.lineCountry.setGeometry(QtCore.QRect(230, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineCountry.setFont(font)
        self.lineCountry.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineCountry.setObjectName("lineCountry")
        self.comboBoxGammePrix = QtWidgets.QComboBox(self.widget)
        self.comboBoxGammePrix.setGeometry(QtCore.QRect(90, 260, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.comboBoxGammePrix.setFont(font)
        self.comboBoxGammePrix.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;\n"
"")
        self.comboBoxGammePrix.setEditable(False)
        self.comboBoxGammePrix.setMaxVisibleItems(3)
        self.comboBoxGammePrix.setObjectName("comboBoxGammePrix")
        self.comboBoxGammePrix.addItem("")
        self.comboBoxGammePrix.addItem("")
        self.comboBoxGammePrix.addItem("")
        self.labelHeureOuverture = QtWidgets.QLabel(self.widget)
        self.labelHeureOuverture.setGeometry(QtCore.QRect(60, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelHeureOuverture.setFont(font)
        self.labelHeureOuverture.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelHeureOuverture.setObjectName("labelHeureOuverture")
        self.timeEditHeureDebut = QtWidgets.QTimeEdit(self.widget)
        self.timeEditHeureDebut.setGeometry(QtCore.QRect(210, 310, 71, 31))
        self.timeEditHeureDebut.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.timeEditHeureDebut.setObjectName("timeEditHeureDebut")
        self.labelVisite2 = QtWidgets.QLabel(self.widget)
        self.labelVisite2.setGeometry(QtCore.QRect(280, 320, 20, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelVisite2.setFont(font)
        self.labelVisite2.setStyleSheet("")
        self.labelVisite2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVisite2.setObjectName("labelVisite2")
        self.timeEditHeureFin = QtWidgets.QTimeEdit(self.widget)
        self.timeEditHeureFin.setGeometry(QtCore.QRect(300, 310, 71, 31))
        self.timeEditHeureFin.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.timeEditHeureFin.setObjectName("timeEditHeureFin")
        self.checkBoxFaitLivraison = QtWidgets.QCheckBox(self.widget)
        self.checkBoxFaitLivraison.setGeometry(QtCore.QRect(90, 360, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.checkBoxFaitLivraison.setFont(font)
        self.checkBoxFaitLivraison.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.checkBoxFaitLivraison.setObjectName("checkBoxFaitLivraison")
        self.labelError = QtWidgets.QLabel(self.widget)
        self.labelError.setGeometry(QtCore.QRect(0, 390, 400, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setText("")
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.buttonBoxOkRetour = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour.setGeometry(QtCore.QRect(430, 910, 171, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.buttonBoxOkRetour.setFont(font)
        self.buttonBoxOkRetour.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOkRetour.setCenterButtons(True)
        self.buttonBoxOkRetour.setObjectName("buttonBoxOkRetour")
        self.buttonBoxOkRetour_2 = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour_2.setGeometry(QtCore.QRect(250, 580, 171, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.buttonBoxOkRetour_2.setFont(font)
        self.buttonBoxOkRetour_2.setStyleSheet("")
        self.buttonBoxOkRetour_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBoxOkRetour_2.setCenterButtons(True)
        self.buttonBoxOkRetour_2.setObjectName("buttonBoxOkRetour_2")
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
        self.labelEditResto.setText(_translate("MainWindow", "Modifier un  Restaurant"))
        self.lineRestoName.setText(_translate("MainWindow", "Nom du Restaurant"))
        self.lineTypeNourriture.setText(_translate("MainWindow", "Type de Nourriture"))
        self.lineAdRue.setText(_translate("MainWindow", "Rue"))
        self.lineAdVille.setText(_translate("MainWindow", "Ville"))
        self.lineAdPostal.setText(_translate("MainWindow", "Code Postal"))
        self.lineAdNum.setText(_translate("MainWindow", "Numero"))
        self.lineCountry.setText(_translate("MainWindow", "Pays"))
        self.comboBoxGammePrix.setItemText(0, _translate("MainWindow", "Prix bas"))
        self.comboBoxGammePrix.setItemText(1, _translate("MainWindow", "Prix moyen"))
        self.comboBoxGammePrix.setItemText(2, _translate("MainWindow", "Prix haut"))
        self.labelHeureOuverture.setText(_translate("MainWindow", "Heure d\'Ouverture"))
        self.labelVisite2.setText(_translate("MainWindow", "-"))
        self.checkBoxFaitLivraison.setText(_translate("MainWindow", "Fait Livraison"))
from . import res_rc
