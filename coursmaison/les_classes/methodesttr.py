class Personne:
    
    def __init__(self):
        self.test = "true"
        self.jeu = "wow"
        self.age = 20

    def __setattr__(self, nom__atrr, val_atrr):


        object.__setattr__(self,nom__atrr,val_atrr)
        self.enregistrer()
