"""en python on peux attribuer des propriétés à des classes, qui permette de modifier les attribut de maniere plus propre
voir doc pour plus d'info"""
class Personne:
    
    def __init__(self):
        self.pseudo = "bod"
        self._lieu_residence = "Paris"

    def _get_lieu_residence(self):


        print("on accede au lieu de résidence")
        return self._lieu_residence 
    def _set_lieu_residence(self,nouvelle_residance):
        print("hey have you see that {} move to {}".format(self.pseudo,nouvelle_residance))
        self._lieu_residence = nouvelle_residance
 # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


test = Personne()
test.lieu_residence = "Chicago"

