"""dans ce programme on va mettre des arguments dans la fonction init"""
class Personnes:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.habite = "Mexico"


bod = Personnes("bod",12)
a = bod.age
b = bod.name
c = bod.habite
print(a,b,c)
