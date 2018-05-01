from PySide import QtGui
from noteui.fenetrePricipal import Ui_MainWindow
import main as nm
import utils as utl
import os
class CreateurDeNote(QtGui.QWidget, Ui_MainWindow):
    def __init__(self):
        super(CreateurDeNote, self).__init__()
        self.setupUi(self)
        self.recuperlanote()
        self.setupConnections()
        self.show()
    def setupConnections(self):
        self.btn_addnote.clicked.connect(self.creernote)
        self.lw_listeDeNotes.itemClicked.connect(self.afficherlanote)
        self.btn_updatenote.clicked.connect(self.mettreajourlanote)
        self.btn_removenote.clicked.connect(self.supprimerlanote)
    def creernote(self):
        nomDeLaNote, ok = QtGui.QInputDialog.getText(self,'add a note', 'enter the name of the note: ')
        if not ok: 
            return
        nm.creeNote(nomDeLaNote)
        self.recuperlanote()
    def recupenoteselect(self):
        notesselect = self.lw_listeDeNotes.selectedItems()
        if not notesselect:
            return
        nomDeLaNote = notesselect[-1].text()
        cheminDeLaNote = os.path.join(utl.DATA_FOLDER, nomDeLaNote + '.txt')
        print(nomDeLaNote, cheminDeLaNote)
        return nomDeLaNote, cheminDeLaNote
    def afficherlanote(self):
        nomDeLaNote, cheminDeLaNote = self.recupenoteselect()
        contenuDeLaNote = nm.recupererLeContenu(nomDeLaNote)
        self.te_contenuDeLaNote.setText(contenuDeLaNote)
    def supprimerlanote(self):
        nomDeLaNote, cheminDeLaNote = self.recupenoteselect()
        nm.supprimerNote(nomDeLaNote)
        self.recuperlanote()
        self.te_contenuDeLaNote.setText('')
    def mettreajourlanote(self):
        nomDeLaNote, cheminDeLaNote = self.recupenoteselect() 
        contenuDeLaNote = self.te_contenuDeLaNote.toPlainText()
        nm.creeNote(nomDeLaNote,contenuDeLaNote)
    def recuperlanote(self):
        self.lw_listeDeNotes.clear()
        notes = nm.recupererlesNote()
        self.lw_listeDeNotes.addItems(notes)
app = QtGui.QApplication([])
a = CreateurDeNote()
app.exec_()
        
