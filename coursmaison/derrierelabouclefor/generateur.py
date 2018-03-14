import os
print("loading please wait ... ")
def intervalle(borneinf,bornsup):
    borneinf += 1
    while borneinf<bornsup:
        yield borneinf
        borneinf += 1
for nb in intervalle(0,101):
    
    os.system("sleep 1")
    print(nb)
def fct():

    generateur = intervalle(10, 25)
    for nombre in generateur:
        if nombre == 15: # On saute à 20
            generateur.send(20)
        print(nombre, end=" ")
