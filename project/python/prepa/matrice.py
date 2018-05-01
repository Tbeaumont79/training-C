#programme matrice
import numpy
#mise en application du pivot de gauss
def matriceO(n,p):
    #initialisation de la matrice
    """    A = []
    #ajout de n ligne
    for i in range(n):
        L = []
        for j in range(p):
            L.append(0)
        
        A.append(L)
    """  
    A = [[0 for j in range (p)]for i in range (n)]
    print(A)
def matrice(i,j):
    A = []    

b = matriceO(6,11)
for i in range (6):
    for j in range (11):
        b[i][j] = i-j
