from PySide import QtGui, QtCore
class FenetrePrinipale(QtGui.QWidget):
    def __init__(self):
        super(FenetrePrinipale, self).__init__()
        self.setWindowTitle('les signaux')
        layout = QtGui.QHBoxLayout(self)
        btn = QtGui.QPushButton('clique')
        btn.clicked.connect(self.cliquersurlebouton)
        layout.addWidget(btn)
    def cliquersurlebouton(self):
        print("l'utilisateur a cliquer !'")
    

app = QtGui.QApplication([])
Fenetre = FenetrePrinipale()
Fenetre.show()
app.exec_()
