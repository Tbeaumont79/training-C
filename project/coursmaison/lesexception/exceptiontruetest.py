year = input("entrez une année : ")


try:
     year = int(year)

     if year < 0:
        raise ValueError("cela peut-être négatif?")
     print("nice tu as écris",year)
     assert year > 2000#assert permet de verifier si une condition est respecter si elle ne l'est pas elle renvoie
   #une erreur
except ValueError:
    print("erreur : tu devrais écrire un chiffre, OH LE SEGPA")
except AssertionError:
    pass


finally:
    print("Fin du programme..")
#tu peux crée une erreur en fesant raise :

