from PySide import QtCore,QtGui
from ui.ui import Ui_Fenettreprincipal
import main
class playListe(QtGui.QWidget,):
    def __init__(self):
        super(playListe, self).__init__()
        self.setupUi(self)
        self.setupConnection()
        self.show()
    def setupConnection(self):
        pass


