#auteur : thibault
#objectif: calculer les racines d'un polynome
import math

#declaration de notre fonctionpolynom
print("caculons les racines du polynome")
a = float(input("avec a = "))
b = float(input("avec b = "))
c = float(input("avec c = "))
d = b**2-4*a*c

if d < 0:
     print("notre polynome n'admet pas de racine dans R")
elif d > 0:
         x1 = (-b-math.sqrt(d))/(2*a)
         x2 = (-b+math.sqrt(d))/(2*a)
         print("les racines sont",x1,"et",x2)
else:
    x1 = (-b-math.sqrt(d))/(2*a)
    print("on a une unique racine dans R")
    
    

