import math as m


def racine(a,b,c):
    
    print("calculons le discriminant")
    if a == 0:
      print("erreur")
    else:
         d = b**2-4*a*c
    
         if d > 0:
                x1 = (-b-m.sqrt(d))/(2*a)
                x2 = (-b+m.sqrt(d))/(2*a)
                print("notre polynome admet deux racines qui sont",x1,"et",x2)
   
         elif d == 0:
                x1 = (-b)/(2*a)
                print("notre polynome admet une racine qui est ",x1)
   
         else :

             x1 = (-b-1j*m.sqrt(-d))/(2*a)
             x2 = (-b+1j*m.sqrt(-d))/(2*a)
             print("notre polynome admet deux racines",x1,"et",x2)

    return(x1,x2)


racine(3,2,5)
