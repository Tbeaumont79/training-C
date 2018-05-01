def decorateur(classe):
    print("Definition de la classe {0}".format(classe))
    @decorateur
    class test:
        pass
decorateur()
