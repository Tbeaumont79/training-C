"""ce programme a pour but d'intégrer des notions mathématiques dans les classes"""

class Duree:
    def __init__(self, min=0 , sec=0):
        

        self.min = min
        self.sec = sec

    def __str__(self):
        
        return "{0:02} : {1:02}".format(self.min,self.sec)
    def __add__(self, objet_a_ajouter):
        nouvelle_duree = Duree()
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec

        nouvelle_duree.sec += objet_a_ajouter
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        return nouvelle_duree

test = Duree(3,53)
