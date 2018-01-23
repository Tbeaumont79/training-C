class Yop: 
    def __init__(self):
        """on défini un attribut"""
        self.yo = "hi"
    def afficher_attribut(self):
        """methode affichant l'attribut yo'"""
        print("mon attribut est {0}".format(self.yo))
    
    
    

io = Yop()
io.afficher_attribut
a = dir(io)
print(a)
