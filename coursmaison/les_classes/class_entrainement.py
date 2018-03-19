import os
class Personage : 
    def __init__(self,pos,life_health,power,your_class,stamin,ressources):
        self.position = pos
        self.life =  life_health
        self.powerfull = power
        self.type = your_class
        self.stamina = stamin
        self.mana = ressources
    def is_alive(self):
        return (self.life > 0)

    
    def mouvement(self,DH,DY):
        self.position[0] = self.position[0] + DH
        self.position[1] = self.position[1] + DY
class Action_On_class(Personage):
    def __int__(self):
        super()
    
    def mage():
        #cast du mage différent sort:
        spell = set(["firebolt","icebolt","arcanepower","arcane missil","food"])
        cast = input("choose your spell among : {} enter the name of the spell : ".format(spell))
        if cast in spell:
            for i in range(3):
                os.system("sleep 1")
                i += 1
                print(i)
            if cast == "food":print("food is ready ")
            return(spell)
        else:
            raise ImportError("not a good spell")
        #gestion du déplacement du mage
        #ajout de keyEvent
    def hunter():
        pass
    def warrior():
        pass
    def shaman():
        pass
    def priest():
        pass


def class_choose_function():
    class_available = set(["mage","warrior","hunter","priest","shaman"]).__str__()
    class_choose = input("choose your class among :"+ class_available +"   write the class that you want : ")
    if class_choose in class_available:
        pass
    if class_choose == "mage":
        Action_On_class.mage()
    else:
        raise ImportError("choose a class that exist ! ")
def main():
        player = input("enter the name of your character. ").__str__()
        if len(player) > 10:
                raise ValueError("The name of your your character is too long .")
        player = Action_On_class([0,20],100,80,class_choose_function(),30,100)
                


        #boss
        gardien = Personage([0,0],100,50,"Mage",20,None)
        lo_thar = Personage([10,0],100,80,"Warrior",60,None)
if __name__ == "__main__":
    main()