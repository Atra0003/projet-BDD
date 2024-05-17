# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClientAddNote.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AjouterNote(object):
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
        self.labelAddNote = QtWidgets.QLabel(self.widget)
        self.labelAddNote.setGeometry(QtCore.QRect(80, 0, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(20)
        self.labelAddNote.setFont(font)
        self.labelAddNote.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAddNote.setObjectName("labelAddNote")
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
        self.dateEditVisite = QtWidgets.QDateEdit(self.widget)
        self.dateEditVisite.setGeometry(QtCore.QRect(80, 140, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.dateEditVisite.setFont(font)
        self.dateEditVisite.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.dateEditVisite.setObjectName("dateEditVisite")
        self.labelVisite = QtWidgets.QLabel(self.widget)
        self.labelVisite.setGeometry(QtCore.QRect(80, 90, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelVisite.setFont(font)
        self.labelVisite.setObjectName("labelVisite")
        self.plainTextEditCommentaire = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEditCommentaire.setGeometry(QtCore.QRect(20, 180, 351, 141))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.plainTextEditCommentaire.setFont(font)
        self.plainTextEditCommentaire.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.plainTextEditCommentaire.setDocumentTitle("")
        self.plainTextEditCommentaire.setObjectName("plainTextEditCommentaire")
        self.spinBoxNote = QtWidgets.QSpinBox(self.widget)
        self.spinBoxNote.setGeometry(QtCore.QRect(220, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.spinBoxNote.setFont(font)
        self.spinBoxNote.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;")
        self.spinBoxNote.setMaximum(5)
        self.spinBoxNote.setObjectName("spinBoxNote")
        self.labelVisiteNote = QtWidgets.QLabel(self.widget)
        self.labelVisiteNote.setGeometry(QtCore.QRect(130, 330, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.labelVisiteNote.setFont(font)
        self.labelVisiteNote.setObjectName("labelVisiteNote")
        self.comboBoxRecommendation = QtWidgets.QComboBox(self.widget)
        self.comboBoxRecommendation.setGeometry(QtCore.QRect(80, 380, 251, 31))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.comboBoxRecommendation.setFont(font)
        self.comboBoxRecommendation.setStyleSheet("border-image: url(:/Images/Beige2.png);\n"
"border-radius:10px;\n"
"")
        self.comboBoxRecommendation.setEditable(False)
        self.comboBoxRecommendation.setMaxVisibleItems(3)
        self.comboBoxRecommendation.setObjectName("comboBoxRecommendation")
        self.comboBoxRecommendation.addItem("")
        self.comboBoxRecommendation.addItem("")
        self.comboBoxRecommendation.addItem("")
        self.buttonBoxOkRetour = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBoxOkRetour.setGeometry(QtCore.QRect(250, 590, 171, 16))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.buttonBoxOkRetour.setFont(font)
        self.buttonBoxOkRetour.setMouseTracking(False)
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
        self.labelAddNote.setText(_translate("MainWindow", "Ajouter une Note"))
        self.lineEditRestoName.setText(_translate("MainWindow", "Nom du Restaurant"))
        self.labelVisite.setText(_translate("MainWindow", "Date de Visite"))
        self.plainTextEditCommentaire.setPlainText(_translate("MainWindow", "Ecriver votre commentaire..."))
        self.labelVisiteNote.setText(_translate("MainWindow", "Note"))
        self.comboBoxRecommendation.setItemText(0, _translate("MainWindow", "Recommande"))
        self.comboBoxRecommendation.setItemText(1, _translate("MainWindow", "Deconseille"))
        self.comboBoxRecommendation.setItemText(2, _translate("MainWindow", "A Eviter d\'urgence"))
from . import res_rc
