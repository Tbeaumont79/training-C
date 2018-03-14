
#DM d informatique Siwar
from math import *
import matplotlib.pyplot as plt
#on défini u(0)
u=1
def calculeduniemetermesdelasuiteun(n):
     #on utilise global u qui nous permet d'utiliser notre premier termeu(0)'
    global u
#calcule de la suite a l aide d une boucle for
    for j in range(1,(n+1)):
        """on stocke la valeur de u dans une variable a chaque iteration"""
        a = u
        #calcule de notre suite
        u = log(2-a)
        #on affiche les termes de notre suite.
        print(u)


calculeduniemetermesdelasuiteun(100)
def convergence1(p):
    u=1
    L=0.442854401002
    k=0                         #Initialisation du rang
    while( abs(u-L)>=10**-p):
        u=log(2-u)
        k=k+1                   #Incrémentation du rang
    print("Le rang ou Un est proche de L a 10**-p est",k)
    return(k)


#Partie 2:Méthode de la dichotomie

#Question 1/
def suitea_b(n) :               #Definition des suites (a_n) et (b_n)
   a=0                          #Premier terme de (a_n)
   b=4                          #Premier terme de (b_n)
   i=0                          #Initialisation de la boucle
   while i<n :
         if exp((a+b)/2)+((a+b)/2)-2>0 : #Calcul du n-ième terme de la suite
             b=((a+b)/2)
         else :
             a=((a+b)/2)
         i=i+1
   return a,b                   #Retour du resultat de la fonction


#Question 2/

def convergence2(p):            #Définition de la fonction
    a=0                         #Premier terme de (a_n)
    b=4                         #Premier terme de (b_n)
    c=0.442854401002
    n=1                         #initialisation de n
    while abs(b-c)>10**-p :
         if exp((a+b)/2)+((a+b)/2)-2>0 : #calcul de b(n+1)
             b=((a+b)/2)
         else :
             a=((a+b)/2)
         n=n+1                  #incrémentation de n

    return n                    #Retour de la fonction

    if p<=0 or p>=15:
        print("erreur de saisie")
    else :
        print('p= ', p,'n=',convergence2(p))


#Partie 3

#Question 1/
def suiteX(n):                  #Definition de la suite (X_n)
    X=4                         #Premier terme de la suite (X_n)
    for i in range(1,n+1):
        X=X-((exp(X)+X-2)/(exp(X)+1))   #Formule de la suite X= X-f(X)/f'(X)
                                #Calcul de la valeur n-ieme de la suite
    return(X)                   #Retour de la valeur de X

#Question 2/
def convergence3(p):
    if p >= 0 and p <= 15:      #la variable p doit être comprise entre 0 et 15
        n=1                     #Initialisation de la boucle
        while(suiteX(n)-0.442854401002 >= 10**(-p)):
              n=n+1             #Incrémentation de n
        print("Le premier rang de n tel que X_n - 0.442854401002 <= 10**(-p)")
    return(n)


#Partie 4: Comparaison des vitesses de convergence3

def comparaison():
    X = list(range(1,13))
    Y = [convergence1(x) for x in X]
    plt.show()
    Z = [convergence2(x) for x in X]
    plt.show()
    U = [convergence3(x) for x in X]
    plt.show()

    
    plt.plot(X,Y,color ='r',label ='Méthode n°1')
    plt.plot(X,Z,color ='b',label ='Méthode n°2:Dichotomie')
    plt.plot(X,U,color ='g',label ='Méthode n°3:Newton')
    plt.title("la vitesse de l'operation' du point d'anulation de f")
    plt.legend(loc=2)
comparaison()
     #La méthode la plus rapide est celle de Newton
        
