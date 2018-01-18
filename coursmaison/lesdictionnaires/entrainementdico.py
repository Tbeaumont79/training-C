"""ce programme fait appelle au items contenue dans moyenne"""
"""l'utilisateur entre ses differents moyennes"""
math = int(input("entre ta moyenne en math "))
physique = int(input("entre ta moyenne en physique "))
anglais = int(input("entre ta moyenne en anglais "))
moyenne ={'math':math,'physique':physique,'anglais':anglais}
for clef,value in moyenne.items():
    print("ta moyenne en {} corespond à {}".format(clef,value))
    if value < 10:
        print("tu n'a pas la moyenne")
    elif value > 20:
        raise TypeError("ta moyenne doit etre comprise entre 0 et 20")
        
    else:
        print("bien !")

