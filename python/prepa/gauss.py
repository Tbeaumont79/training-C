#fichier : gauss.py
#auteur : prof TSI1
#date : mars 2016

#Objectif : Algorithme du pivot de Gauss à compléter.

#-------------  imports  --------------

#import numpy as np #si vous êtes avez numpy

#------------  Programme  -------------
#---------------------------------------

def dimension(A):
    n=len(A)
    m=len(A[0])
    for i in range(n):
        assert len(A[i])==m, "ce n'est pas une bonne matrice"
    return n,m

#---------------------------------------

def copie_matrice(A):
    
    n,m = dimension(A)
    B = [[A[i][j]for i in range(m)]for j in range(n)]
    print(B)
    #Test fonction copie_matrice
    print("\nTEST FONCTION copie_matrice")
    A=[[1,9,5],[8,3,7],[2,6,4]]
    print("1) A vaut :", A)
    B=copie_matrice(A)
    print("   en faisant B=copie_matrice(A), B vaut :", B)
    print("\n   modifions A en tapant A[0][0]=100")
    A[0][0]=100
    print("   A vaut maintenant :",A)
    print("   et B vaut :", B)
    print("   si seulement A a été modifié (pas B), votre fonction fonctionne.")

copie_matrice([0,0,0],[0,0,0])
def echange_lignes(A,i,j): #on echange les deux lignes L_i et L_j.
    n,m=dimension(A)
    for k in range(m):
        A[i][k],A[j][k]=A[j][k],A[i][k]

#Test fonction echange_lignes
print("\nTEST FONCTION echange_lignes")
A=[[1,9,5],[8,3,7],[2,6,4]]
Y=[[10],[20],[30]]
print("1) ce que vaut A initialement :", A)
print("   ce que renvoie echange_lignes(A,0,1) :", echange_lignes(A,0,1))
print("   ce que vaut maintenant A :", A)
print("2) ce que vaut Y initialement :", Y)
print("   ce que renvoie echange_lignes(Y,0,1) :", echange_lignes(Y,0,1))
print("   ce que vaut maintenant Y :", Y)

#----------------------------------------

def transvection(A,i,j,mu): #on réalise l'opération L_i <- L_i + mu * L_j
    n,m=dimension(A)
    for k in range(m):
            A[i][k]= A[i][k] + mu*A[j][k]
    # à compléter
    

#Test fonction transvection
print("\nTEST FONCTION transvection")
A=[[1,9,5],[8,3,7],[2,6,4]]
Y=[[10],[20],[30]]
print("1) ce que vaut A initialement :", A)
print("   ce que renvoie transvection(A,2,0,-2) :", transvection(A,2,0,-2))
print("   ce que vaut maintenant A :", A)
print("2) ce que vaut Y initialement :", Y)
print("   ce que renvoie transvection(Y,2,0,-2) :", transvection(Y,2,0,-2))
print("   ce que vaut maintenant Y :", Y)

#-----------------------------------------

def dilatation(A,i, nu): #On effectue l'opération L_i <- 1/mu L_i
    n,m=dimension(A)
    # à compléter

#Test fonction dilatation
print("\nTEST FONCTION dilatation")
A=[[1,9,5],[8,3,7],[2,6,4]]
Y=[[10],[20],[30]]
print("1) ce que vaut A initialement :", A)
print("   ce que renvoie dilatation(A,2,2) :", dilatation(A,2,2))
print("   ce que vaut maintenant A :", A)
print("2) ce que vaut Y initialement :", Y)
print("   ce que renvoie dilatation(Y,2,2) :", dilatation(Y,2,2))
print("   ce que vaut maintenant Y :", Y)

#------------------------------------------

def indice_pivot(A,i): #on cherche quel est l'indice du maximum des éléments A[i][i],A[i+1][i],...,A[n-1][i] en valeurs absolues, avec n le nombre de lignes.
    n,m=dimension(A)
    Maxi = abs([A][i][i])
    position = 1
    for k in range (i+1,n):
        if Maxi < ([A][k][i]):
            Maxi = abs([A][i][k])
            position = Maxi
        return position

#Test fonction indice_pivot
print("\nTEST FONCTION indice_pivot")
A=[[1,9,5],[8,3,7],[2,6,4]]
print("si A vaut :", A)
print("indice_pivot(A,0) renvoie :", indice_pivot(A,0))
A=[[1,9,5],[8,3,7],[200,6,4]]
print("si A vaut :", A)
print("indice_pivot(A,0) renvoie :", indice_pivot(A,0))
A=[[100,9,5],[8,3,7],[2,6,4]]
print("si A vaut :", A)
print("indice_pivot(A,0) renvoie :", indice_pivot(A,0))

#------------------------------------------

def gauss(A0,Y0): #renvoie le vecteur colonne X tel que A0*X=Y0, on suppose qu'il existe.
    A=copie_matrice(A0)
    n,m=dimension(A)
    assert n==m, "La matrice A n'est pas carrée"
    m,p=dimension(Y0)
    assert m==n, "Le nombre de lignes de A et Y n'est pas le même"
    assert p==1, "Y n'est pas un vecteur"
    Y=copie_matrice(Y0)
    # à compléter

#Test fonction gauss
print("\nTEST FONCTION gauss")
A=[[1,1,1],[1,-1,2],[2,-1,1]]
Y=[[2],[9],[7]]
print("1) pour A = ", A)
print("   et Y = ", Y)
print("   on doit obtenir = [[1.0], [-2.0], [3.0]]")
X=gauss(A,Y)
print("   Vous obtenez :", X)

#------------------------------------------

#Complexité en temps de l'algorithme
print("\nComplexité en temps de l'algorithme")

from random import randint

print("\nTEST")
def soit(n):
    # à compléter

#Test fonction soit
print("\nTEST FONCTION soit")
print("soit(5) renvoie :", soit(5))
print("soit(5) renvoie :", soit(5))
print("soit(5) renvoie :", soit(5))

#Temps de calcul :

import time

X=[]
Y=[]
for i in range(1,41):
    n=5*i
    print('n =',n)
    
    t0=time.time()
    test(n)
    t1=time.time()
    print(' temps ',(t1-t0))
    X.append(n)
    Y.append(t1-t0)
"""



    
