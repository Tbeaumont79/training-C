"""gerer l'inscription du jouer """
from fonction import * 
from donnees import *
prenom = input("entrez votre prenom : ")
print("trés bien {} bienvenue sur le jeu du pendue --- les régles sont simple tu as 8 chances au départ --- tu dois trouvers les lettres parmis les mots choisi aléatoirement --- si tu arrive à trouver le mot et qu'il te reste 3 chances tu auras 3 points.--- bon courage ---".format(prenom))
fonction_replace()
key = 0
while key != len(pick):
    key1 = input("entre une lettre ")
    if key1 in pick:
        print("nice tu as trouver une lettre est {}".format(key1))
        key += 1

    else:
        print("tu as perdu une chances ")
        nombre_de_chance = nombre_de_chance - 1
        print("il te reste ",nombre_de_chance,"chances")
        if nombre_de_chance == 0:
            print("t'es pendu")
            quit()
"""scores = { prenom: 0 }
print(scores)"""
"""création d'une fonction créant un fichier Text dans lequel les scores seront enregistrer"""
"""création du fichier score"""
    





