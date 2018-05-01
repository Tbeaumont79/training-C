#beaumont
from math import sqrt
#fonction obtention de polynome
a = 0
b = 0
c = 0

def fonctionpolynome(a,b,c):
    #déclaration de a,b,c
    a = int(input(a))
    b = int(input(b))
    c = int(input(c))
    de = (b**2)-4*a*c
    if de < 0:
        print("il n'y a pas de solution réel")
    elif de > 0:
        print("notre polynome admet deux racines qui sont")
        r1 = (-b-sqrt(de))/2*a
        r2 = (-b+sqrt(de))/2*a
        print(r1,r2)
    elif de == 0:
        print("notre polynome admet une unique solution dans R")
        r3 = (-b)/2*a
        return(r3)
fonctionpolynome(a,b,c)
