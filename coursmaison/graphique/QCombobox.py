from PySide import QtGui,QtCore
class Fenettreprincipal(QtGui.QWidget):
    def __init__(self):
        super(Fenettreprincipal, self).__init__()
        self.setWindowTitle('Mon Application')
        layout = QtGui.QHBoxLayout(self)
        cbb_demo = QtGui.QComboBox()
        cbb_demo.addItems(['address','age','name'])
        cbb_demo.setCurrentIndex(cbb_demo.count() - 1)
        layout.addWidget(cbb_demo)

app = QtGui.QApplication([])
fenetre = Fenettreprincipal()
fenetre.show()
app.exec_()


