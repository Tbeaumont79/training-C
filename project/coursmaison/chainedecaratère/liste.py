"""le but est simple il faut faire une liste qui contier le nombre de fruit et déclaré une variable avec le nombre de fruit à retirer """
fruit_a_retirer = 7
liste = [15,3,18,21]
affichage = [nb_fruits-fruit_a_retirer for nb_fruits in liste if nb_fruits>fruit_a_retirer]
print(affichage)
