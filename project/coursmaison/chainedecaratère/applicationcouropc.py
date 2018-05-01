"""petit exercice faire une fonction afficher identique a print, c'est à dire choisir un nombre indéterminer de paramètre, les affichants les séparent à l'aide du paramètre nommé sep et terminant l'affichage par la variable fin """
def affichage(sep =' ', *parametres,fin="\n " ):
    parametres = list(parametres)
    for i,parametre in enumerate (*parametres):
        parametres[i] = str(parametre)
    chainedecaratere = sep.join((parametres)
    chainedecaratere += fin
    print(chainedecaratere,fin= ' ')
affichage(["yo"],["eh"])
