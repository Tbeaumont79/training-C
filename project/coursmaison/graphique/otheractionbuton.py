from PySide import QtGui,QtCore
from functools import partial
class FenetrePrincipale(QtGui.QWidget):

    def __init__(self):
        super(FenetrePrincipale,self).__init__()
        self.setWindowTitle('les signaux')
        layout =  QtGui.QHBoxLayout(self)
        btn_01 = QtGui.QPushButton('Premier bouton')
        btn_01.clicked.connect(partial(self.boutonClicked,'premier bouton clique'))
        btn_02 = QtGui.QPushButton('Second bouton')
        btn_02.clicked.connect(partial(self.boutonClicked,'deuxieme bouton clique'))
        layout.addWidget(btn_01)
        layout.addWidget(btn_02)

    def boutonClicked(self, text):
        print(text)

        

app = QtGui.QApplication([])
fenetre = FenetrePrincipale()
fenetre.show()
app.exec_()
