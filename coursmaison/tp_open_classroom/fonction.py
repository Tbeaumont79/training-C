"""coding : utf_8"""
"""fonction du système du jeu"""
from donnees import Words,nombre_de_chance
import random
import pickle
"""fonction"""
pick = random.choice(Words)
mot_alea = len(pick) * '*'
def fonction_replace():
    global pick
    global mot_alea
    global nombre_de_chance
    print("c'est un mot en {} lettre".format(len(pick)),pick)
    tab = list(mot_alea)
    key = 0
    while pick != mot_alea:
        if key < nombre_de_chance:
            print("mot random : ", mot_alea)
            lettre = input("entrez une lettre : ")
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
                print("il te reste ",nombre_de_chance-key,"chance")
            if pick == mot_alea:
                print("nice tu as trouver le mots ")
                print("vous avez ",key," score")
            elif key == nombre_de_chance:
                print("vous n'aviez que ",nombre_de_chance,"chance")
                quit()
                        
                    
def Creation_score_file():
    scores = { prenom: nombre_de_chance }
    with open('score','wb') as score:
        my_pickler = pickle.Pickler(score)
        score_total = my_pickler.dump(scores)
        print(score_total)

