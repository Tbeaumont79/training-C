class Protege: 
    """class possédant une méthode particulière d'accées a ses atribut : 
    si l'atribut n'est pas trouver on affichera une alerte et le programme renverra none """
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
    def __getattr__(self, nom):
        """si python ne trouve pas cette méthode il renvoit une erreur"""
        print("Attention, il n'y a pas d'atribut {} ici ".format(nom)) 
test = Protege()
test.g
