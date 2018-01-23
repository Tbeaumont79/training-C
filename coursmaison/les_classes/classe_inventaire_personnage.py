"""on ajoute a tout cela une petite gestion d'erreur"""
try:
    class Inventory: 
        
        def __init__(self):

            self.arms = "sword"
            self.shoulder = "shoulder"
            self.chest = "chest"
            self.legs = "legs"
            self.boots = "boots"
        def stuff_diamond(cls):

            diamond = int(input("type 1 for a diamond stuff : "))
            if diamond == 1:
                print("you have a {} and a {} and a {} and a {} and a {} in diamond  ".format(inv.arms,inv.shoulder,inv.chest,inv.legs,inv.boots))
            else:
                print("you want another stuff ? type yes or no")
                answer = input("write yes or no  : ")
                if answer == "yes" or answer == "Yes":
                    print("okay !")
                    print("you have a {} and a {} and a {} and a {} and a {} in obsidian".format(inv.arms,inv.shoulder,inv.chest,inv.legs,inv.boots))
                else:
                    pass

        stuff_diamond = classmethod(stuff_diamond)

    inv = Inventory()
    inv.stuff_diamond()
except ValueError:
    print("il a une erreur")
except TypeError:
    print("fais attention aux consignes")
