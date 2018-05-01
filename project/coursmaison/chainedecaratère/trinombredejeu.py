"""ce sotfware est simple il constitu à ranger les jeux par leurs ordres"""


def listedejeux():

    liste_de_jeux = [
        ("wow",4),
        ("lol",6),
        ("Minecraft",8),
        ("Diablo3",29),

    ]
    liste_de_jeux_inverse = [(nbjeux,qtt) for qtt,nbjeux in liste_de_jeux ]
    liste_de_jeux_inverse.sort(reverse=True)
    listedejeux = [(qtt,nbjeux) for nbjeux,qtt in liste_de_jeux ]
    print(liste_de_jeux)
listedejeux()
