# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientCheckResto.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsulterResto(object):
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
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        self.widget.setFont(font)
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.labelCheckOpinion = QtWidgets.QLabel(self.widget)
        self.labelCheckOpinion.setGeometry(QtCore.QRect(10, 0, 391, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.labelCheckOpinion.setFont(font)
        self.labelCheckOpinion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCheckOpinion.setObjectName("labelCheckOpinion")
        self.lineCheckRestoName = QtWidgets.QLineEdit(self.widget)
        self.lineCheckRestoName.setGeometry(QtCore.QRect(80, 40, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineCheckRestoName.setFont(font)
        self.lineCheckRestoName.setTabletTracking(False)
        self.lineCheckRestoName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineCheckRestoName.setObjectName("lineCheckRestoName")
        self.labelInfoResto = QtWidgets.QLabel(self.widget)
        self.labelInfoResto.setGeometry(QtCore.QRect(80, 80, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoResto.setFont(font)
        self.labelInfoResto.setStyleSheet("")
        self.labelInfoResto.setObjectName("labelInfoResto")
        self.labelInfoRestoAdRue = QtWidgets.QLabel(self.widget)
        self.labelInfoRestoAdRue.setGeometry(QtCore.QRect(70, 120, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoRestoAdRue.setFont(font)
        self.labelInfoRestoAdRue.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoRestoAdRue.setObjectName("labelInfoRestoAdRue")
        self.labelInfoGammePrix = QtWidgets.QLabel(self.widget)
        self.labelInfoGammePrix.setGeometry(QtCore.QRect(80, 240, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoGammePrix.setFont(font)
        self.labelInfoGammePrix.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoGammePrix.setObjectName("labelInfoGammePrix")
        self.labelInfoTypeNourriture = QtWidgets.QLabel(self.widget)
        self.labelInfoTypeNourriture.setGeometry(QtCore.QRect(80, 280, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoTypeNourriture.setFont(font)
        self.labelInfoTypeNourriture.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoTypeNourriture.setObjectName("labelInfoTypeNourriture")
        self.labelInfoRestoAdVille = QtWidgets.QLabel(self.widget)
        self.labelInfoRestoAdVille.setGeometry(QtCore.QRect(240, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoRestoAdVille.setFont(font)
        self.labelInfoRestoAdVille.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoRestoAdVille.setObjectName("labelInfoRestoAdVille")
        self.labelInfoRestoAdPays = QtWidgets.QLabel(self.widget)
        self.labelInfoRestoAdPays.setGeometry(QtCore.QRect(240, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoRestoAdPays.setFont(font)
        self.labelInfoRestoAdPays.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoRestoAdPays.setObjectName("labelInfoRestoAdPays")
        self.labelInfoRestoAdNumero = QtWidgets.QLabel(self.widget)
        self.labelInfoRestoAdNumero.setGeometry(QtCore.QRect(70, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoRestoAdNumero.setFont(font)
        self.labelInfoRestoAdNumero.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoRestoAdNumero.setObjectName("labelInfoRestoAdNumero")
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
        self.labelInfoRestoAdCodePostal = QtWidgets.QLabel(self.widget)
        self.labelInfoRestoAdCodePostal.setGeometry(QtCore.QRect(140, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoRestoAdCodePostal.setFont(font)
        self.labelInfoRestoAdCodePostal.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoRestoAdCodePostal.setObjectName("labelInfoRestoAdCodePostal")
        self.checkBoxFaitLivraison = QtWidgets.QCheckBox(self.widget)
        self.checkBoxFaitLivraison.setGeometry(QtCore.QRect(80, 360, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.checkBoxFaitLivraison.setFont(font)
        self.checkBoxFaitLivraison.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.checkBoxFaitLivraison.setObjectName("checkBoxFaitLivraison")
        self.labelHeureOuverture = QtWidgets.QLabel(self.widget)
        self.labelHeureOuverture.setGeometry(QtCore.QRect(100, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelHeureOuverture.setFont(font)
        self.labelHeureOuverture.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelHeureOuverture.setObjectName("labelHeureOuverture")
        self.labelHeureFermeture = QtWidgets.QLabel(self.widget)
        self.labelHeureFermeture.setGeometry(QtCore.QRect(230, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelHeureFermeture.setFont(font)
        self.labelHeureFermeture.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelHeureFermeture.setObjectName("labelHeureFermeture")
        self.labelVisite2 = QtWidgets.QLabel(self.widget)
        self.labelVisite2.setGeometry(QtCore.QRect(190, 330, 20, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.labelVisite2.setFont(font)
        self.labelVisite2.setStyleSheet("")
        self.labelVisite2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelVisite2.setObjectName("labelVisite2")
        self.labelInfoEvaluation = QtWidgets.QLabel(self.widget)
        self.labelInfoEvaluation.setGeometry(QtCore.QRect(80, 200, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelInfoEvaluation.setFont(font)
        self.labelInfoEvaluation.setStyleSheet("border-image: url(:/Images/Beige2.png);")
        self.labelInfoEvaluation.setObjectName("labelInfoEvaluation")
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
        self.labelCheckOpinion.setText(_translate("MainWindow", "Consulter des Restaurants"))
        self.lineCheckRestoName.setText(_translate("MainWindow", "Nom du Restaurant"))
        self.labelInfoResto.setText(_translate("MainWindow", "Informations du Restaurant"))
        self.labelInfoRestoAdRue.setText(_translate("MainWindow", "Rue du Restaurant"))
        self.labelInfoGammePrix.setText(_translate("MainWindow", "Gamme de Prix"))
        self.labelInfoTypeNourriture.setText(_translate("MainWindow", "Type de Nourriture"))
        self.labelInfoRestoAdVille.setText(_translate("MainWindow", "Ville"))
        self.labelInfoRestoAdPays.setText(_translate("MainWindow", "Pays"))
        self.labelInfoRestoAdNumero.setText(_translate("MainWindow", "Numero"))
        self.labelInfoRestoAdCodePostal.setText(_translate("MainWindow", "Code Postal"))
        self.checkBoxFaitLivraison.setText(_translate("MainWindow", "Fait Livraison"))
        self.labelHeureOuverture.setText(_translate("MainWindow", "Ouverture"))
        self.labelHeureFermeture.setText(_translate("MainWindow", "Fermeture"))
        self.labelVisite2.setText(_translate("MainWindow", "-"))
        self.labelInfoEvaluation.setText(_translate("MainWindow", "Evaluation"))
from . import res_rc
