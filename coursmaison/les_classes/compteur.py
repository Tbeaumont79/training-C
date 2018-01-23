class Compteur:
    starter = 0
    def __init__(self):
        Compteur.starter += 1
        self.name = "bod"
        self.test = "programing"
        self.level = "in extension"


    def afficher_compteur(cls):
        print("le nombre d'attribut est {0}".format(cls.starter))
    afficher_compteur = classmethod(afficher_compteur)


a = Compteur()
b = Compteur()
print("my name is  {} i am {} and my level is {}".format(a.name,a.test,a.level))
Compteur.afficher_compteur()
"""entrainement de class"""
