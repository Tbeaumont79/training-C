def afficher_flotant(flottant):
    if type(flottant) is not float:
        raise TypeError("choisissez un flottant")
    flottant = str(flottant)
    partientier, partiflottante = flottant.split(".")
    a = ",".join ([partientier,partiflottante[:3]])
    print(a)
afficher_flotant(3.666677543564567)

