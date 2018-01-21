"""gerer l'inscription du jouer """
from fonction import * 
from donnees import *
prenom = input("entrez votre prenom : ")
print("trés bien {} bienvenue sur le jeu du pendue --- les régles sont simple tu as 8 chances au départ --- tu dois trouvers les lettres parmis les mots choisi aléatoirement --- si tu arrive à trouver le mot et qu'il te reste 3 chances tu auras 3 points.--- bon courage ---".format(prenom))
fonction_replace()

"""création d'une fonction créant un fichier Text dans lequel les scores seront enregistrer"""
"""création du fichier score"""    
