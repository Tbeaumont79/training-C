from PySide import QtGui

app = QtGui.QApplication([])
label = QtGui.QLabel('hello dude')
button = QtGui.QPushButton('clique dessus')
label.show()
button.show()
app.exec_()
