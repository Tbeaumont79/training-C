from PySide import QtGui
app = QtGui.QApplication([])

lineEdit = QtGui.QLineEdit()

lineEdit.setPlaceholderText('yo push the button')
lineEdit.show()
lineEdit.clearFocus()
app.exec_()

