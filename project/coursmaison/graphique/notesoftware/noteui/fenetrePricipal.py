# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fenetrePrincipale.ui'
#
# Created: Sat Feb  3 19:44:21 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 516)
        self.fenetrePrincipale = QtGui.QWidget(MainWindow)
        self.fenetrePrincipale.setObjectName("fenetrePrincipale")
        self.gridLayout = QtGui.QGridLayout(self.fenetrePrincipale)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_addnote = QtGui.QPushButton(self.fenetrePrincipale)
        self.btn_addnote.setObjectName("btn_addnote")
        self.gridLayout.addWidget(self.btn_addnote, 0, 0, 1, 1)
        self.btn_removenote = QtGui.QPushButton(self.fenetrePrincipale)
        self.btn_removenote.setObjectName("btn_removenote")
        self.gridLayout.addWidget(self.btn_removenote, 0, 1, 1, 1)
        self.lw_listeDeNotes = QtGui.QListWidget(self.fenetrePrincipale)
        self.lw_listeDeNotes.setObjectName("lw_listeDeNotes")
        self.gridLayout.addWidget(self.lw_listeDeNotes, 1, 0, 2, 2)
        self.te_contenuDeLaNote = QtGui.QTextEdit(self.fenetrePrincipale)
        self.te_contenuDeLaNote.setObjectName("te_contenuDeLaNote")
        self.gridLayout.addWidget(self.te_contenuDeLaNote, 1, 2, 1, 1)
        self.btn_updatenote = QtGui.QPushButton(self.fenetrePrincipale)
        self.btn_updatenote.setObjectName("btn_updatenote")
        self.gridLayout.addWidget(self.btn_updatenote, 2, 2, 1, 1)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Note creator", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_addnote.setText(QtGui.QApplication.translate("MainWindow", "add note", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_removenote.setText(QtGui.QApplication.translate("MainWindow", "remove note", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_updatenote.setText(QtGui.QApplication.translate("MainWindow", "update note", None, QtGui.QApplication.UnicodeUTF8))

