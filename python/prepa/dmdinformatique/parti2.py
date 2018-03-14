#BEAUMONT THIBAULT
#Partie 2 : Methode de la dichotomie
#on defini a(0) et b(0) 
from math import *
a = 0
b = 4
def calcule_des_nieme_termes(an,bn):
    global a,b
#calule de an
    for a in range (1,(an+1)):
        if (exp((an+bn)/2)+(an+bn)/2-2) > 0:
            print(an)
        else:
            print((an+bn)/2)

#calcule de bn
    for b in range(1,(bn+1)):
        if (exp((an+bn)/2)+(an+bn)/2-2) > 0:
            print((an+bn)/2)
        else:
            print(bn)
    def convergence2(p):
        result = bn - 0.442854401002
        if abs(result)<= 10**-(p):
            print("pour p = 7 le premier rang n est : ", result)
    convergence2(12)
calcule_des_nieme_termes(24,31)
