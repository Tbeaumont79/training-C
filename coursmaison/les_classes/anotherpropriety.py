import os
class Agedeplus:
    
    def __init__(self):
        self.prenom = "Thibault"
        self._age = 20
        self.job = "informatique"
    def _get_age(self):
        

        print("on accede a l'age de l'utilisateur")
        return self._age
    def _set_age(self,nouvelle):

        print("{} tu as pris un ans de plus tu as {} ans ".format(self.prenom,nouvelle))
        self._age = nouvelle

    age = property(_get_age,_set_age)

test = Agedeplus()
test.age = 21
if test.age >= 21 and test.prenom == "Thibault":
    os.system("say 'it will be okay HAPPYBIRTHDAY !!!'")
    
