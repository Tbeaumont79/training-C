# fichier : compare_age.py
#auteur : thibault
#date : octobre 2017
#objectif : comparer l'age de l'utilisateur et celui du voisin 
#----------------- Programme -----------------------
try:
    ageU = int(input("quel est votre age ? "))
    ageV = int(input("quel est l'age de votre voisin? "))
    if ageU > ageV:
        print("vous etes plus vieux")
    elif ageU < ageV:
        print("vous etes plus jeune")
    else:
        print("vous avez le meme age")
except ValueError:
    print("c'est valeur n'est pas possible")
except KeyboardInterrupt:
    print("fermeture du programme")

