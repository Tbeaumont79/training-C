"""project creation de logiciel """
import os
from glob import glob
import utils as utl
def recupererLeContenu(nomDeLaNote):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER,nomDeLaNote +'.txt')
    with open(cheminDeLaNote,'r') as f:
        contenuDeLaNote = f.read()

    return contenuDeLaNote
def creeNote(nomDeLaNote, contenu = ''):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER,nomDeLaNote +'.txt')
    with open(cheminDeLaNote,'w') as f:
        f.write(contenu)
        if os.path.isfile(cheminDeLaNote):
            print('la note "{}" a bien ete cree'.format(nomDeLaNote))


def supprimerNote(nomDeLaNote):
    cheminDeLaNote = os.path.join(utl.DATA_FOLDER,nomDeLaNote + '.txt')

    if os.path.isfile(cheminDeLaNote):
        os.remove(cheminDeLaNote)
        print('la note "{}" a bien ete supprimer'.format(nomDeLaNote))

    else:
        print('la note {} n existe pas '.format(nomDeLaNote))
def recupererlesNote():
    notes = glob(utl.DATA_FOLDER + '/*.txt')
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]
    
    return(notes)

supprimerNote('test1')
