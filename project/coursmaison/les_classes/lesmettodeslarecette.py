import os
os.system("say 'this programme show the power of class in python you should work on it'")


class TableauNoir:


    def __init__(self):
        self.surface = ""

    def ecrire(self, message_a_ecrire):
             """Méthode permettant d'écrire sur la surface du tableau.Si la surface n'est pas vide, on saute une ligne avant de rajouter le message à écrire"""
             
             if self.surface != "":
                self.surface += "\n"
             self.surface += message_a_ecrire
    def lire(self):
        print(self.surface)
        
    def erase(self):
        self.surface = ""



tab = TableauNoir()
tab.ecrire("hey we are in hollyday")
tab.lire()

tab.erase()
