#auteur : Beaumont
#programme pour annee bisextil
annee = int(input("donnez une annee "))
r4 = annee % 4
r100 = annee % 100
r400 = annee % 400
if r4 == 0 or (r100 != 0 and r400 == 0): #anne est divisible par 4 ssi le reste est egale a 0
    print("bisextil")
else:
    print("non bisextil")

