# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RestaurateurStat.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Stats(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 895)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(:/Images/DesignBgr.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 160, 391, 441))
        self.widget.setStyleSheet("border-radius:50px;\n"
"border-image: url(:/Images/Beige1.png);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 421, 51))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineRestoName = QtWidgets.QLineEdit(self.widget)
        self.lineRestoName.setGeometry(QtCore.QRect(90, 60, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.lineRestoName.setFont(font)
        self.lineRestoName.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.lineRestoName.setAlignment(QtCore.Qt.AlignCenter)
        self.lineRestoName.setObjectName("lineRestoName")
        self.labelNbrAvis = QtWidgets.QLabel(self.widget)
        self.labelNbrAvis.setGeometry(QtCore.QRect(90, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNbrAvis.setFont(font)
        self.labelNbrAvis.setStyleSheet("")
        self.labelNbrAvis.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNbrAvis.setObjectName("labelNbrAvis")
        self.labelNbrAvisRes = QtWidgets.QLabel(self.widget)
        self.labelNbrAvisRes.setGeometry(QtCore.QRect(250, 150, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNbrAvisRes.setFont(font)
        self.labelNbrAvisRes.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelNbrAvisRes.setText("")
        self.labelNbrAvisRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNbrAvisRes.setObjectName("labelNbrAvisRes")
        self.labelNoteMoyenne = QtWidgets.QLabel(self.widget)
        self.labelNoteMoyenne.setGeometry(QtCore.QRect(40, 200, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNoteMoyenne.setFont(font)
        self.labelNoteMoyenne.setStyleSheet("")
        self.labelNoteMoyenne.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNoteMoyenne.setObjectName("labelNoteMoyenne")
        self.labelNoteMoyenneRes = QtWidgets.QLabel(self.widget)
        self.labelNoteMoyenneRes.setGeometry(QtCore.QRect(250, 200, 200, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNoteMoyenneRes.setFont(font)
        self.labelNoteMoyenneRes.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelNoteMoyenneRes.setText("")
        self.labelNoteMoyenneRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNoteMoyenneRes.setObjectName("labelNoteMoyenneRes")
        self.labelPlatPopulaire = QtWidgets.QLabel(self.widget)
        self.labelPlatPopulaire.setGeometry(QtCore.QRect(90, 290, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelPlatPopulaire.setFont(font)
        self.labelPlatPopulaire.setStyleSheet("")
        self.labelPlatPopulaire.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlatPopulaire.setObjectName("labelPlatPopulaire")
        self.labelPlatPopulaireRes = QtWidgets.QLabel(self.widget)
        self.labelPlatPopulaireRes.setGeometry(QtCore.QRect(90, 330, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelPlatPopulaireRes.setFont(font)
        self.labelPlatPopulaireRes.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelPlatPopulaireRes.setText("")
        self.labelPlatPopulaireRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPlatPopulaireRes.setObjectName("labelPlatPopulaireRes")
        self.labelStat = QtWidgets.QLabel(self.widget)
        self.labelStat.setGeometry(QtCore.QRect(100, 110, 261, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelStat.setFont(font)
        self.labelStat.setObjectName("labelStat")
        self.labelError = QtWidgets.QLabel(self.widget)
        self.labelError.setGeometry(QtCore.QRect(0, 370, 400, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(10)
        self.labelError.setFont(font)
        self.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.labelError.setText("")
        self.labelError.setAlignment(QtCore.Qt.AlignCenter)
        self.labelError.setObjectName("labelError")
        self.labelNoteMoyenneLivraisonRes = QtWidgets.QLabel(self.widget)
        self.labelNoteMoyenneLivraisonRes.setGeometry(QtCore.QRect(250, 240, 200, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNoteMoyenneLivraisonRes.setFont(font)
        self.labelNoteMoyenneLivraisonRes.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.labelNoteMoyenneLivraisonRes.setText("")
        self.labelNoteMoyenneLivraisonRes.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNoteMoyenneLivraisonRes.setObjectName("labelNoteMoyenneLivraisonRes")
        self.labelNoteMoyenneLivraison = QtWidgets.QLabel(self.widget)
        self.labelNoteMoyenneLivraison.setGeometry(QtCore.QRect(40, 240, 191, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelNoteMoyenneLivraison.setFont(font)
        self.labelNoteMoyenneLivraison.setStyleSheet("")
        self.labelNoteMoyenneLivraison.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNoteMoyenneLivraison.setObjectName("labelNoteMoyenneLivraison")
        self.buttonBoxOkRetour = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour.setGeometry(QtCore.QRect(250, 570, 171, 16))
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
        self.label.setText(_translate("MainWindow", "Statistiques"))
        self.lineRestoName.setText(_translate("MainWindow", "Nom du Restaurant"))
        self.labelNbrAvis.setText(_translate("MainWindow", "Nombre d\'Avis"))
        self.labelNoteMoyenne.setText(_translate("MainWindow", "Note Moyenne Service"))
        self.labelPlatPopulaire.setText(_translate("MainWindow", "Plat Populaire"))
        self.labelStat.setText(_translate("MainWindow", "Statistique sur le Restaurant"))
        self.labelNoteMoyenneLivraison.setText(_translate("MainWindow", "Note Moyenne Livraison"))
from . import res_rc
