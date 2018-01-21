from math import ceil
from random import randrange
try:
    nombrechoisie = int(input("entrez un nombre entre 0 et 50 : "))
    if nombrechoisie > 50 or nombrechoisie < 0:
        print("ce nombre ne correspond pas a l'intervalle demander")
    else:
        a = nombrechoisie//2
        user_moneyaccount = 200
        while user_moneyaccount >= 0:
            argent = int(input("entrez une mise : "))
            if argent <= 0:
                raise ValueError
            elif argent > user_moneyaccount:
                print("tu ne peux pas miser l'argent que tu n'as pas")
                quit()
            #demander une mise si la mise est negative sa renvoie une erreur
            if nombrechoisie == 2*a:
                print("la couleur est noir")
            else:
                print("la couleur est rouge")
            #associer la couleur rouge si c'est impaire
            #associer la couleur noir si c'est pair
                     #demander a l'utilisateur un nombre entre 0 et 50
            nombreramdome = randrange(0,50)
            print("le nombre choisie par la machine est",nombreramdome)
            #gener un nombre entre 0 et 50
            if nombrechoisie == nombreramdome:
                print("vous avez gagnez bravo votre mise est multiplier pas 3")
                user_moneyaccount = user_moneyaccount+(argent * 3)
            #si le nombre est bon on triple le gain
            elif nombrechoisie != nombreramdome and nombrechoisie == 2*a:
                print("nombre faux,la couleur,bonne donc tu as 50 % des gains")
                user_moneyaccount = user_moneyaccount+(argent * 0.5)
        #si le nombre est faux mais la couleur est bonne on donne 50 % du gain
            elif nombrechoisie != nombreramdome and nombrechoisie == 2*(a+1):
                print("Nombre faux,la couleur est bonnes tu as 50% des gains")
            else:
            #si l'utilisateur a perdu on lui affiche le montant restant
                user_moneyaccount = argent - user_moneyaccount
                if user_moneyaccount <= 0:
                    print("ta loose ",argent-user_moneyaccount,"$")
                    print("tu n'as plus d'argent ! ")
                    print("il te reste : ",ceil(user_moneyaccount)," $")
                    quit()
        #si c'est perdu loose total
        # arrondir les resultats
            print("il te reste : ",ceil(user_moneyaccount)," $")
            print("souhaite tu continuer ?\n oui ou non ?")
            reponse = input("")
        
            if reponse == "oui":
                print("le jeu continu !")
            elif reponse == "non":
                print("d'accord merci d'avoir jouer aurevoir")
                quit()
            elif reponse != "oui" or reponse != "non":
                print("entrez oui ou non !")
                quit()

                
except ValueError:
#si jamais l'utilisateur utilise autre chose qu'un nombre on renvoie une erreur
    print("entrez un chiffre ou une valeur correcte")
except KeyboardInterrupt:
    print("Le programme ne repond plus")
