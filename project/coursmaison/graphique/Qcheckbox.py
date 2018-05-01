from PySide import QtGui, QtCore
import sys
class FenetrePrincipal(QtGui.QWidget):
    def __init__(self):
        super(FenetrePrincipal,self).__init__()
        self.setWindowTitle('mon application')
        layout = QtGui.QHBoxLayout(self)
        chk_demo = QtGui.QCheckBox('ceci est une checkbox')
        layout.addWidget(chk_demo)
app = QtGui.QApplication(sys.argv)
win = FenetrePrincipal()
win.show()
sys.exit(app.exec_())


