#auteur: beaumont thibault  
#date: 05/12/17
#objectif: maitrisez les boucles for

def somme(n):
    S=0 #on initialise notre somme à 0
    for i in range(1,n+1):
        S = S+i
    return(S)
def produit(l):
     p=0
     for k in range(1,l+1):
        p+=p*k
     print(p)
