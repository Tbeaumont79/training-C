"""coding : utf_8"""
"""fonction du système du jeu"""
from donnees import Words,nombre_de_chance
import random
import pickle
import os
"""fonction"""



def main():

    while 1:
        pick = random.choice(Words)
        mot_alea = len(pick) * '*'
        prenom = input("enter your name : ")
        os.system("say 'okay thank you, rules are easy you have 8 trys if you find a letter, you will see by yourself '")
        global nombre_de_chance
        print("it's a word in {} letter".format(len(pick)),pick)
        tab = list(mot_alea)
        key = 0
        while pick != mot_alea:
            if key < nombre_de_chance:
                print("mot random : ", mot_alea)
                lettre = input("enter a letter: ")
                if lettre in pick:
                    i = 0
                    for c in pick:
                        if c == lettre:
                            tab[i] = lettre
                        i += 1
                    mot_alea = ''
                    for c in tab:
                        mot_alea += c
                else:
                    key+= 1
                    print("you have  ",nombre_de_chance-key,"try's left")
                if pick == mot_alea:
                    os.system("say 'nice you found it !'")
                    print("your score is  ",nombre_de_chance-key)
                elif key == nombre_de_chance:
                    print("you only had ",nombre_de_chance,"try ")
                    os.system("say 'unfortunatly it's done for you , you are dead ")
                    quit()
                            
                        
        
        scores = { prenom: nombre_de_chance-key }
        with open('score','wb') as score:
            my_pickler = pickle.Pickler(score)
            score_total = my_pickler.dump(scores)
        with open('score','rb') as score:
            my_depickler = pickle.Unpickler(score)
            scored = my_depickler.load()
            print(scored)
        os.system("say 'Do you want to stop ? write yes , if you want to stop'")
        stopornot = input("write yes if you want to stop !: ")    
        if stopornot == "yes" or stopornot == "Yes":
            quit()
        else:
            os.system("say 'ok please write you name ! '")
            
