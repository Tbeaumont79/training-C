from PySide import QtGui,QtCore
from intelo import Ui_Form
class FenettrePrincipale(QtGui.QWidget,Ui_Form):
    def __init__(self):
        super(FenettrePrincipale,self).__init__()
        self.setupUi(self)
        self.show()
app = QtGui.QApplication([])
fenettre = FenettrePrincipale()
fenettre.show()
app.exec_()



