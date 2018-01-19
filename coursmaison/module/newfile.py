"""on peux crée des fichier en python grace au module pickle"""
import pickle
"""on ajoute un dictionnaire a notre fichier"""
fruit = {
    "pommes": 5,
    "fraise": 6,
    "abricot": 12,
    "poire" : 24,

}
def creatingfileswithvalues ():
    with open('helloworld','wb') as fichier:
        my_pickler = pickle.Pickler(fichier)
        inventaire = my_pickler.dump(fruit)
        
"""afin de pouvoir afficher parfaitement le dictionnaire on fait ajoute une autre fonction qui load notre dictionnaire"""
def deplickerfonction ():
    with open('helloworld','rb') as fichier:
        my_depickler = pickle.Unpickler(fichier)
        inventaire_fruit = my_depickler.load()
        print(inventaire_fruit)
deplickerfonction()
"""En résumé ce code crée un fichier dans lequel est placer un dictionnaire lorsque l'on appelle la fonction creatingfileswithvalues le dictionnaire est en binaire et donc incompréhensible pour les humains mais grace à notre deuxième fonction on Unpickler le fichier et cela devient nettement plus comprehensible.'"""
