"""gerer l'inscription du jouer """
from fonction import * 
from donnees import *
import os
os.system("say 'hello welcome, to bod corporation, here we are making things great for the world, if you want to play the game, please write yes !'")
anser = input("write yes if you want to continue and no if you want to stop : ")
if anser == 'yes' or anser == 'Yes':
    os.system("say 'okay ,first i would like to know your name, Please write your name'")
    main()
    
else:
    os.system("say 'fine, we hope to see you again, you already miss us'")
"""création d'une fonction créant un fichier Text dans lequel les scores seront enregistrer"""
"""création du fichier score"""    
