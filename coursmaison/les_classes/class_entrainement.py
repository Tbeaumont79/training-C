import os
class Personage: 
    def __init__(self,pos,life_health,power,your_class,stamin,ressources):
        self.position = pos
        self.life =  life_health
        self.powerfull = power
        self.type = your_class
        self.stamina = stamin
        self.mana = ressources
    def is_alive(self):
        return (self.life > 0)
    def attack(self):
        pass
    
    def mouvement(self,DH,DY):
        self.position[0] = self.position[0] + DH
        self.position[1] = self.position[1] + DY
class Mage:

    def __init__(self):
        #cast du mage différent sort:
        self.spell = ["firebolt","icebolt","arcanepower","arcane missil","food"]
        cast = input("choose your spell among : {} enter the name of the spell : ".format(self.spell))
        
    def spell_use(self):
        if self.cast in self.spell:
            for i in range(3):
                os.system("sleep 1")
                i += 1
                print(i)
            if self.cast == "food":print("food is ready ")
            return(spell)
        else:
            raise ImportError("not a good spell")
        #gestion du déplacement du mage
        #ajout de keyEvent
class Hunter:
    def __init__(self):

        self.spell= ["kill shot","disengage","cobra shot"]
        self.cast = input("choose the spell that you want among {} : ".format(self.spell))
        
    def spell_use(self):

        if self.cast in self.spell:
            if self.cast == "disengage":
                return self.cast
            for i in range(3):
                i+=1
                print(i)
        else:raise ImportError("spell not found")


class Warrior:
    def __init__(self):

        self.spell = ["charge","heroic leap","inrage"]
        self.cast = input("choose your attack among : {} :".format(self.spell))
    def action_use(self):

        if self.cast in self.spell:
            if self.cast == "inrage":
                    return self.cast
            else:
                for i in range('3'):
                    os.system("sleep 3")
                    i += 1
                    print(1)
        if self.cast not in self.spell:raise ImportError("spell not found")
class Shaman:
    def __init__(self):
    
        self.spell = ["bl", "totem","lava burst","small heal", "ligthing bolt"]
        self.cast = input("choose your speel among {} ".format(self.spell))
    def spell_use(self):

        if self.cast in self.spell:
            if self.cast == "bl" or self.cast == "totem":
                return self.cast
            else:
                for i in range(3):
                    os.system("sleep 3")
                    i+=1
                    print(i)
        if self.cast not in self.spell:raise ImportError("spell not found")
class Priest:
    def __init__(self):

        self.spell = ["small heal","greater heal", "absorb buble","fear"]
        self.cast = input("choose your spell among {} : ".format(self.spell))
    def spell_use(self):
        if self.cast == self.spell[2] or self.cast == self.spell[3]:
            return self.spell[2] or self.spell[3]
        else:
            for i in range(3):
                os.system("sleep 3")
                i+=1
                print(i)

        if self.cast not in self.spell:print("can't reach the speel !")

def class_choose_function():
    class_available = set(["mage","warrior","hunter","priest","shaman"]).__str__()
    class_choose = input("choose your class among :"+ class_available +"   write the class that you want : ")
    if class_choose in class_available:
    
        if class_choose == "mage":
            Mage().spell_use()
        elif class_choose =="hunter":
            Hunter().spell_use()
        elif class_choose == "priest":
            Priest().spell_use()
        elif class_choose == "shaman":
            Shaman().spell_use()
        elif class_choose == "warrior":
            Warrior().action_use()
    
    else:raise ImportError("choose a class that exist ! ")
def main():
        player = input("enter the name of your character. ").__str__()
        if len(player) > 10:
                raise ValueError("The name of your your character is too long .")
        player = Personage([0,20],100,80,class_choose_function(),30,100)
                


        #boss
        gardien = Personage([0,0],100,50,"Mage",20,None)
        lo_thar = Personage([10,0],100,80,"Warrior",60,None)
if __name__ == "__main__":
    main()