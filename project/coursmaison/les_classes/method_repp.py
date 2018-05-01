class Personne:
    def __init__(self):
        self.prenom = "bod"
        self.age = 15
    """méthode spécial repr """        
    def __repr__(self):
        return "prenom {} a {} ans".format(self.prenom,self.age)
test = Personne()
print(test)
