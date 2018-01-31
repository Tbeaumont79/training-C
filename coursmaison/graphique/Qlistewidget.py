from PySide import QtGui 
class FenetrePrincipal(QtGui.QWidget):
    def __init__(self):
        super(FenetrePrincipal, self).__init__()

        layout = QtGui.QHBoxLayout(self)
        lw_demo = QtGui.QListWidget(self)
        lw_demo.addItems(['bod','test','bonjour'])
        lw_demo.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        layout.addWidget(lw_demo)
        
app = QtGui.QApplication([])
fenetre = FenetrePrincipal()
fenetre.show()
app.exec_()
