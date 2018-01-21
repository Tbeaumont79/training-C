"""coding : utf_8"""
"""fonction du système du jeu"""
from donnees import Words
import random
import pickle
"""fonction"""
pick = random.choice(Words)
def fonction_replace():
    global pick
    print("c'est un mot en {} lettre".format(len(pick)),pick)
    
def Creation_score_file():
    with open('score','wb') as score:
        my_pickler = pickle.Pickler(score)
        score_total = my_pickler.dump(score_by_name)


