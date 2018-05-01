import os
def listelesfichier():
    a = input("voulez vous lister les fichiers dans votres dossier ? (Y/N) ")
    if a == 'y' or a == 'Y':
        os.system("ls")
    else:
        pass
listelesfichier()
