from PySide import QtGui
class MonApplication(QtGui.QWidget):
    def __init__(self):
        super(MonApplication, self).__init__()
        layout = QtGui.QVBoxLayout(self)
        btn_1 = QtGui.QPushButton('bouton 1',self)
        btn_2 = QtGui.QPushButton('bouton 2', self)
        btn_3 = QtGui.QPushButton('bouton 3', self)
        btn_4 = QtGui.QPushButton('bouton 4', self)
        btn_5 = QtGui.QPushButton('bouton 5', self)
        layout.addWidget(btn_1)
        layout.addWidget(btn_2)
        layout.addWidget(btn_3)
        layout.addWidget(btn_4)
        layout.addWidget(btn_5)
        self.resize(500,500)

app = QtGui.QApplication([])
fenetre = MonApplication()
fenetre.show()
app.exec_()
