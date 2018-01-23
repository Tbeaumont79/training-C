class Test:
    """une class de Test tous simplement"""
    def afficher():
        print("on affiche la meme chose")
        print("peu importe les données ou les objects de la classs")

    afficher = staticmethod(afficher)
    print(afficher)

