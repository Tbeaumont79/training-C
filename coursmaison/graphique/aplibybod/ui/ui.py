# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenettreprincipal.ui'
#
# Created: Sun Feb  4 11:39:43 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Fenettreprincipal(object):
    def setupUi(self, Fenettreprincipal):
        Fenettreprincipal.setObjectName("Fenettreprincipal")
        Fenettreprincipal.resize(618, 522)
        Fenettreprincipal.setStyleSheet("*{\n"
"background-color : rgb(28, 24, 41)\n"
"}")
        self.centralWidget = QtGui.QWidget(Fenettreprincipal)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.playList = QtGui.QListWidget(self.centralWidget)
        self.playList.setAutoFillBackground(False)
        self.playList.setTabKeyNavigation(False)
        self.playList.setProperty("showDropIndicator", False)
        self.playList.setMovement(QtGui.QListView.Static)
        self.playList.setObjectName("playList")
        self.gridLayout.addWidget(self.playList, 0, 0, 1, 3)
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 2, 1, 1)
        self.time_music = QtGui.QProgressBar(self.centralWidget)
        self.time_music.setProperty("value", 24)
        self.time_music.setObjectName("time_music")
        self.gridLayout.addWidget(self.time_music, 2, 0, 1, 3)
        Fenettreprincipal.setCentralWidget(self.centralWidget)

        self.retranslateUi(Fenettreprincipal)
        QtCore.QMetaObject.connectSlotsByName(Fenettreprincipal)

    def retranslateUi(self, Fenettreprincipal):
        Fenettreprincipal.setWindowTitle(QtGui.QApplication.translate("Fenettreprincipal", "application 1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Fenettreprincipal", "play", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Fenettreprincipal", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Fenettreprincipal", "repeat", None, QtGui.QApplication.UnicodeUTF8))

