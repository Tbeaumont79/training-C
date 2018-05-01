import os
import time
import random
class Mage:

    def __init__(self):
        self.mana = 100
        self.spell_use()
        dammage = self.dammage
    def spell_use(self):
        #cast du mage différent sort:
        print("type pass if your don't want to use spell")
        self.spell = ["firebolt","icebolt","arcanepower","arcane missil","food","pass"]
        self.cast = input("choose your spell among : {} enter the name of the spell : ".format(self.spell))
        if self.cast in self.spell:
            for i in range(3):
                os.system("sleep 1")
                i += 1
                print(i)
            if self.cast == "food":print("food is ready ")
        if self.cast == self.spell[0]:
            self.dammage = random.randint(20,50)
            print(self.dammage)
            return(self.dammage)
        elif self.cast == self.spell[1]:
            self.dammage = random.randint(15,35)
            print(self.dammage)
        elif self.cast == self.spell[3]:
            self.dammage = random.randint(20,60)
            print(self.dammage)
        elif self.cast == self.spell[4]:
            for i in range(3):
                self.dammage = random.randint(10,30)
                print(self.dammage)
        elif self.cast == self.spell[5]:
            print("okay you decide to pass ! ")
            self.dammage = False
            pass
        return self.cast    
        if self.cast not in self.spell:raise ImportError("not a good spell")
        
class Hunter:
    def __init__(self):
        self.ressources = 100

            
    def spell_use(self):
        self.spell= ["kill shot","disengage","cobra shot"]
        self.cast = input("choose the spell that you want among {} : ".format(self.spell))      
        if self.cast in self.spell:
            if self.cast == "disengage":
                return self.cast
            for i in range(3):
                i+=1
                print(i)
            else:raise ImportError("spell not found")


class Warrior:
    def __init__(self):
        self.rage = 100
        

    def spell_use(self):
        self.spell = ["charge","heroic leap","inrage"]
        self.cast = input("choose your attack among : {} :".format(self.spell))

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
        self.mana = 100

    def spell_use(self):
        self.spell = ["bl", "totem","lava burst","small heal", "ligthing bolt"]
        self.cast = input("choose your speel among {} ".format(self.spell))
        
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
        
        self.mana = 100


    def spell_use(self):
        self.spell = ["small heal","greater heal", "absorb buble","fear"]
        self.cast = input("choose your spell among {} : ".format(self.spell))
        if self.cast == self.spell[2] or self.cast == self.spell[3]:
            return self.spell[2] or self.spell[3]
        else:
            for i in range(3):
                os.system("sleep 3")
                i+=1
                print(i)

        if self.cast not in self.spell:print("can't reach the spell !")
class Ennemie(Mage,Hunter,Shaman,Priest,Warrior):
        def __init__(self,pos,Life_health):
            super()
            self.stat = {"strengh":200}
            self.location = pos
            self.life = Life_health
        def boss_info_stat(self):
            
            while self.life >= 0: 
                self.Class_choose.spell_use()
                spell = ["shockwave","gryphon call","explosion","heroic hit"]
                self.life = self.boss_who.life - self.Class_choose.dammage
                print("the boss life is ",self.life)
                if self.life == 0:
                    print("the boss is dead ! ")
                    pass
                return self.life

class Personage(Ennemie): 
    def __init__(self,pos,life_health,power,stamin):
        super()
        self.position = pos
        self.life =  life_health
        self.powerfull = power
        self.stamina = stamin
        self.breack = os.system("sleep 1")
        self.level = 1
        self.Default_experience = 0
        self.longeur = 25
        self.largeur = 25
        self.area = self.longeur * self.largeur
        self.gardien = Ennemie([0,25,0,0],150000)
        self.lo_thar = Ennemie([25,0,0,0],1000000)
        self.murlock = Ennemie([0,0,50,0],200)
        self.lengendary_boss = [self.murlock,self.gardien,self.lo_thar]
        self.boss = ["gardien","lo_thar","murlock"]
        self.Player_information()
    
        
    def Player_information(self):
        print("your level is ", self.level,"and your experience is ",self.Default_experience)
    def loosing_life(self):
        #loosing 5 pourcent life
        self.loose_life = self.life * (5/100)
        self.life = self.life - self.loose_life

        print(self.life)
    def mouving_function(self):
        print("you have to go back you are in a restricted zone ! 5 seconde left after",
        "you will loose 5 pourcent of your life until you came back in the zone ! ")
        move = ""
            
        while move != "M" or move!= "m":
            start_couting = time.time()
            move = input("type M or m if you want to move ! ")
            stop_couting = time.time()
            if stop_couting - start_couting > 5:
                self.loosing_life()
            if move == "M" or move == "m":
                self.mouvement()
                print(self.position)
                    
            else:
                self.loosing_life()


        else: 
            return self.area 
    def Area(self):
        if self.position[0] >= self.area:
            self.mouving_function()
        elif self.position[1] >= self.area:
            self.mouving_function()
        elif self.position[2] >= self.area:
            self.mouving_function()
        elif self.position[3] >= self.area:
            self.mouving_function()

    def is_alive(self):
        print(self.life)
        if self.life == 0:
            raise ImportWarning("You are dead ")
        else: return self.life

    def aggro(self):
        agro = "AGGRO"
        if self.position == self.lengendary_boss[0].location or self.position == self.lengendary_boss[1].location or self.position == self.lengendary_boss[2].location:
            self.boss_info_stat()
            print(agro)

    



    def attack(self):
            lengendary_boss = self.lengendary_boss
            self.target_focus = input("choose a target among {0} {1} {2} : ".format(self.boss[0],self.boss[1],self.boss[2]))
            if self.target_focus == "Murlock" or self.target_focus == "murlock":
                self.boss_who = self.lengendary_boss[0]
            elif self.target_focus == "lo_thar" or target_focus == "lo thar":
                self.boss_who = self.lengendary_boss[2]
            elif self.target_focus == "gardien" or self.target_focus == "Gardien":
                self.boss_who = self.lengendary_boss[1]  
            while self.life != 0:

                self.boss_info_stat()

            return self.boss_who
            """
            elif self.target_focus not in self.boss:
                raise IndexError("target focus not found !")

            if self.aggro():
                boss_name = self.boss[0]
                set_target_focus = boss_name
                self.Class_choose.spell_use()
        #future fonction ! 

"""
    def mouvement(self):
        mouvement_choose,value= input("where do you want to go ? (z,q,s,d) : ").__str__(),int(input(""))
        if mouvement_choose == "z" and value == int(value):
            self.position[0] = self.position[0] + int(value)
            print(self.position)
            if self.position[0] > self.area:
                self.Area()
            if self.position[0] < self.area:
                self.Action_choose(self.Class_choose)
                return self.position[0]
        
        elif mouvement_choose == "q" and value == int(value):
            self.position[1] = self.position[1] + int(value)
            print(self.position)
            if self.position[1] > self.area:
                self.Area()
            if self.position[1] < self.area:
                self.Action_choose(self.Class_choose)
                return self.position[1]
        elif mouvement_choose == "s" and value == int(value):
            self.position[2] = self.position[2] + int(value)
            print(self.position)
            if self.position[2] > self.area:
                self.Area()
            if self.position[2] < self.area:
                self.Action_choose(self.Class_choose)
                return self.position[2]
        elif mouvement_choose == "d" and value == int(value):
            self.position[3] = self.position[3] + int(value)
            print(self.position)
            if self.position[3] > self.area:
                self.Area()
            if self.position[3] < self.area:
                self.Action_choose(self.Class_choose)
                return self.position[3]
        
        else:  
            raise ValueError("enter a good value : ")

    def Action_choose(self,class_choose):
        self.aggro()
        action = set(["attack","mouvement","use a spell","life stat"])
        Choose_an_action = input("choose an action among {} : ".format(action))
        if Choose_an_action == "attack":
            self.attack()
        elif Choose_an_action == "mouvement":
            self.mouvement()
        elif Choose_an_action == "use a spell":
            self.Class_choose.spell_use()
        elif Choose_an_action == "life stat":
            self.is_alive()

    def class_choose_function(self,player):
        class_available = set(["mage","warrior","hunter","priest","shaman"]).__str__()
        self.class_choose = input("choose your class among :"+ class_available +"   write the class that you want : ")
        if self.class_choose in class_available:
            
            if self.class_choose == "mage":
                self.Class_choose = Mage()
                player.Action_choose(self.Class_choose)
            elif self.class_choose =="hunter":
                self.Class_choose = Hunter()
                player.Action_choose(self.Class_choose)
            elif self.class_choose == "priest":
                self.Class_choose = Priest()
                player.Action_choose(self.Class_choose)
            elif self.class_choose == "shaman":
                self.Class_choose = Shaman()
                player.Action_choose(self.Class_choose)
            elif self.class_choose == "warrior":
                self.Class_choose = Shaman()
                player.Action_choose(self.Class_choose)
            
        else:raise ImportError("choose a class that exist ! ")  

def main():

        player = input("enter the name of your character. ").__str__()
        if len(player) > 10:
            raise ValueError("The name of your your character is too long .")
        player = Personage([0,0,0,0],650,80,None)
        player.class_choose_function(player)

        player.aggro()
        player.Area()
        print(player.position)
        
                #boss
        

        
if __name__ == "__main__":
    main()