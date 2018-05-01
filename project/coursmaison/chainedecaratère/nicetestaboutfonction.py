"""en gros ici on va montrer que les parametres non pas forcement besoin d'etre donné a l'appel de la fonction"""
def information(age,prenom,*commentaire):
    try:
        age = int(age)
        prenom = str(prenom)
        if age > 40: 
            print(" tu a l'age de shakira {}".format(*commentaire))
    except TypeError:
        print("something bad ...")
information(50,"thibault","tu es vieux")
