#auteur : Beaumont Thibault
#objectif tp rendre de la monnaie automatiquement
from fractions import gcd
def pgcd(a,b):
    dividande,diviseur = a,b
    while dividande%diviseur > 0:
        dividande,diviseur=diviseur,dividande % diviseur
    x = diviseur
    print(x) # on retourne le pgcd

def algoglouglou(x):
    restedue = x
    pieces = [200,100,50,20,10,5,2,1]
    arendre = [0,0,0,0,0,0,0,0]
    for i in range (1,len(pieces)):
        while restedue >= pieces[i]:
            arendre[i] = arendre[i]+1
            restedue-=pieces[i]
    print(arendre)

def affichage(pieces,arendre):
    pieces = [200,100,50,20,10,5,2,1]
    arendre = [0,0,0,0,0,0,0,0]
    for i in range(0,len(arendre)):
        print(arendre[i],"pieces de ",pieces[i])
def algoglouglou2(x):
    dico{"pièce de deux euros":0,"pieces d'un euro":0,"pieces de     50 ct":0,"pieces de 20 ct":0,"pieces de 10 ct":0,"pieces de 5    ct":0,"piece de 2 ct":0,"piece de 1 ct":0}
    for i in range(0 len(pieces)):
        while restedue>=pieces[i]:
            dict[pieces[i]] += 1
            restedue = restedue - pieces[i]
    print(dico)
def redudemonnai():
    doit = int(input("entrez la valeur que je vous dois"))
    donner = int(input("entrer une valeur à donner "))
    if donner<doit:
        print("il manque",doit-donner,"centimes")
    else:
        algoglouglou2()
    #cela et faux car dict est un mot réservé)
    #bilan de la sécéance liste et tupple aquis revoir les dico     
