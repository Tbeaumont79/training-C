#auteur: beaumont thibault
#date 5/12/17
#objectif:
# on initialise les variables a et b
from random import randrange
from math import sqrt
def fibonacci(n):
#on intialise nos variables a = F0 et b = F1
    b=0
    a=1
    for k in range(2,n+1):#boucle for pour notre somme
        a,b=a+b,a
    return(a)
#exercice 2
def aleatoire(n):
    n=randrange(1,7)
    print(n)
    k=1
    while n!=6:
        n=randrange(1,7)
        print(n)
        k=k+1
        return(k)
        #exercice 3

def suite (n):
    u=1
    for k in range(1,n+1):
        u=sqrt(u+1)
    print(u)
aleatoire(3)

