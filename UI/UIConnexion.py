# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConnexionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnexionWindow(object):
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
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.labelConnexion = QtWidgets.QLabel(self.widget)
        self.labelConnexion.setGeometry(QtCore.QRect(110, 10, 161, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.labelConnexion.setFont(font)
        self.labelConnexion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelConnexion.setObjectName("labelConnexion")
        self.lineLName = QtWidgets.QLineEdit(self.widget)
        self.lineLName.setGeometry(QtCore.QRect(70, 70, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineLName.setFont(font)
        self.lineLName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineLName.setObjectName("lineLName")
        self.linePassword = QtWidgets.QLineEdit(self.widget)
        self.linePassword.setGeometry(QtCore.QRect(70, 210, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.linePassword.setFont(font)
        self.linePassword.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.linePassword.setObjectName("linePassword")
        self.buttonSignIn = QtWidgets.QPushButton(self.widget)
        self.buttonSignIn.setGeometry(QtCore.QRect(130, 400, 101, 31))
        self.buttonSignIn.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px")
        self.buttonSignIn.setObjectName("buttonSignIn")
        self.lineFName = QtWidgets.QLineEdit(self.widget)
        self.lineFName.setGeometry(QtCore.QRect(70, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineFName.setFont(font)
        self.lineFName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineFName.setObjectName("lineFName")
        self.checkBoxIsRestaurateur = QtWidgets.QCheckBox(self.widget)
        self.checkBoxIsRestaurateur.setGeometry(QtCore.QRect(70, 280, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.checkBoxIsRestaurateur.setFont(font)
        self.checkBoxIsRestaurateur.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.checkBoxIsRestaurateur.setObjectName("checkBoxIsRestaurateur")
        self.checkBoxIsModerateur = QtWidgets.QCheckBox(self.widget)
        self.checkBoxIsModerateur.setGeometry(QtCore.QRect(70, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.checkBoxIsModerateur.setFont(font)
        self.checkBoxIsModerateur.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.checkBoxIsModerateur.setObjectName("checkBoxIsModerateur")
        self.labelError = QtWidgets.QLabel(self.widget)
        self.labelError.setGeometry(QtCore.QRect(40, 370, 311, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setText("")
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
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
        self.labelConnexion.setText(_translate("MainWindow", "Connexion"))
        self.lineLName.setText(_translate("MainWindow", "Nom"))
        self.linePassword.setText(_translate("MainWindow", "Mot de passe"))
        self.buttonSignIn.setText(_translate("MainWindow", "Se connecter"))
        self.lineFName.setText(_translate("MainWindow", "Prenom"))
        self.checkBoxIsRestaurateur.setText(_translate("MainWindow", "Je suis un Restaurateur"))
        self.checkBoxIsModerateur.setText(_translate("MainWindow", "Je suis un Moderateur"))
from .import res_rc