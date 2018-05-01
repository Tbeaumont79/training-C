class Zdict:
    

    def __init__(self):
        self._dico = {}
        

    def __getitem__(self, index):
        

        return self._dico

    def __setitem__(self,index,valeur):

        self._dico[index] = valeur
        
test = Zdict()



