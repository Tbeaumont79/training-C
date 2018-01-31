from PySide import QtGui,QtCore
class FenetrePrincipale(QtGui.QWidget):
    def __init__(self):
        super(FenetrePrincipale,self).__init__()
        self.setWindowTitle('Mon Application')
        layout = QtGui.QHBoxLayout(self)
        prg_demo = QtGui.QProgressBar()
        prg_demo.setRange(0,200)        
        for i in range(190):
            i += 1
            prg_demo.setValue(i)
        layout.addWidget(prg_demo)
app = QtGui.QApplication([])
prg = FenetrePrincipale()
prg.show()
app.exec_()
