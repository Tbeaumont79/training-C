class Compteur:



    object_cree = 0 
    """on crée notre object"""
    def __init__(self):
       Compteur.object_cree += 1

    def combien(cls):
        print("jusqu'a présent {} object on été crée".format(cls.object_cree))
    combien = classmethod(combien)
a = Compteur()
b = Compteur()
#le compteur augmente aprés chaque ajout d'attribut'
Compteur.combien()
