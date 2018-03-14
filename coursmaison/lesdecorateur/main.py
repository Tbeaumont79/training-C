def treufonc(test):

    
    def main():
        print("la fonction appellé est {0} ".format(test))
        return test()
    return main
#globalement la methode reigne sur la fonction elle affecte toute la fonction
@treufonc
def say():
    print("Yo les dude ")
say()
@treufonc
def salut():
    print("coucou")
salut()
