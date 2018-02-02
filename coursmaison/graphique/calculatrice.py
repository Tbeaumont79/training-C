from PySide import QtCore,QtGui
from functools import partial
class Calculatrice(QtGui.QWidget):
    def __init__(self):
        super(Calculatrice,self).__init__()
        self.setWindowTitle('Ma super Calculatrice')
        self.setupUi()
        self.setUpConnections()
        self.show()
    
    def setupUi(self):
        self.le_operation = QtGui.QLineEdit()
        self.le_resultat = QtGui.QLineEdit('0')
        self.gridLayout = QtGui.QGridLayout(self)

        self.button0 = QtGui.QPushButton('0')
        self.button1 = QtGui.QPushButton('1')
        self.button2 = QtGui.QPushButton('2')
        self.button3 = QtGui.QPushButton('3')
        self.button4 = QtGui.QPushButton('4')
        self.button5 = QtGui.QPushButton('5')
        self.button6 = QtGui.QPushButton('6')
        self.button7 = QtGui.QPushButton('7')
        self.button8 = QtGui.QPushButton('8')
        self.button9 = QtGui.QPushButton('9')
        
        self.button_pts = QtGui.QPushButton('.')
        self.button_plus = QtGui.QPushButton('+')
        self.button_moins = QtGui.QPushButton('-')
        self.button_div = QtGui.QPushButton('/')
        self.button_mult = QtGui.QPushButton('x')
        self.button_c = QtGui.QPushButton('C')
        self.button_equal = QtGui.QPushButton('=')

        self.gridLayout.addWidget(self.le_operation, 0,0,1,4)
        self.gridLayout.addWidget(self.le_resultat, 1,0,1,4)
        self.gridLayout.addWidget(self.button_c, 2,0,1,1)
        self.gridLayout.addWidget(self.button_div, 2,3,1,1)
        self.gridLayout.addWidget(self.button7, 3,0,1,1)
        self.gridLayout.addWidget(self.button8, 3,1,1,1)
        self.gridLayout.addWidget(self.button9, 3,2,1,1)
        self.gridLayout.addWidget(self.button_mult, 3,3,1,1)
        self.gridLayout.addWidget(self.button4, 4,0,1,1)
        self.gridLayout.addWidget(self.button5, 4,1,1,1)
        self.gridLayout.addWidget(self.button6, 4,2,1,1)
        self.gridLayout.addWidget(self.button_moins, 4,3,1,1)
        self.gridLayout.addWidget(self.button1, 5,0,1,1)
        self.gridLayout.addWidget(self.button2, 5,1,1,1)
        self.gridLayout.addWidget(self.button3, 5,2,1,1)
        self.gridLayout.addWidget(self.button_plus, 5,3,1,1)
        self.gridLayout.addWidget(self.button0, 6,0,1,1)
        self.gridLayout.addWidget(self.button_pts, 6,2,1,1)
        self.gridLayout.addWidget(self.button_equal, 6,3,1,1)
        self.btns_nombre = []
        for i in range(self.gridLayout.count()):
            
            widget = self.gridLayout.itemAt(i).widget()
            
            if isinstance(widget, QtGui.QPushButton):
                widget.setFixedSize(64,64)
                if widget.text().isdigit():
                    self.btns_nombre.append(widget)
    def setUpConnections(self):
        for btn in self.btns_nombre:
            btn.clicked.connect(partial(self.btn_Nombrepressed, str(btn.text())))
        
        self.button_moins.clicked.connect(partial(self.btn_operationpressed,str(self.button_moins.text())))
        self.button_mult.clicked.connect(partial(self.btn_operationpressed,str(self.button_mult.text())))
        self.button_plus.clicked.connect(partial(self.btn_operationpressed,str(self.button_plus.text())))
        self.button_div.clicked.connect(partial(self.btn_operationpressed,str(self.button_div.text())))
        self.button_equal.clicked.connect(self.calculeOperation)
        
        self.button_c.clicked.connect(self.supprimerleresultat)
    
    def btn_Nombrepressed(self,bouton):
        
        resultat = str(self.le_resultat.text())
        
        if resultat == '0':
            self.le_resultat.setText(bouton)
        
        else:
            self.le_resultat.setText(resultat + bouton)
   
    def btn_operationpressed(self,operation):
        operationTexte = str(self.le_operation.text())
        resultat = str(self.le_resultat.text())
        self.le_operation.setText(operationTexte + resultat + operation)
        self.le_resultat.setText('0')
   
    def supprimerleresultat(self):
        self.le_resultat.setText('0')
        self.le_operation.setText('')
   
    def calculeOperation(self):
        resultat = str(self.le_resultat.text())
        self.le_operation.setText(self.le_operation.text() + resultat)
        resultatOperation = eval(str(self.le_operation.text()))
        self.le_resultat.setText(str(resultatOperation))
        


app = QtGui.QApplication([])
fenetre = Calculatrice()
fenetre.show()
app.exec_()
