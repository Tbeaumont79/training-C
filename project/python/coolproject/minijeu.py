#la regle du jeu est simple vous devez trouver le bon mot l'ordinateur donnes des conseils

#declare un mot

#utilisateur propose un mot si il as faut le pc lui donne un indince

#nombre de  chance limité 

#si l'utilisateur veux quitter il peut
mot = "bonjour"
mot_choisie = ""
i = 0
def depassementdecaractere():
    if mot[i] == len(mot):
        print("l'ordi vous a machez tout le boulot")
        quit()
while mot_choisie != mot:
    mot_choisie = str(input("entrez un mot allez tentez votre chance : "))
    if mot_choisie != mot:
        print("vous avez rater le mot que vous chercher fait ",len(mot)," caractere")
        i = i + 1
        print(mot[i])
        depassementdecaractere()           
