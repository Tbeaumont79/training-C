#fonction en une ligne a l'aide de lambda
#LE PYTHON C'EST PERMISIFFE
g = lambda valeur: valeur * 3
print(g(5))
#une fonction quelconque
def fct(a,b):
    value = a * b
    print(value)
fct(3,5)
"""another type of fonction"""
"""in this fonction you will be able to input the argument of commentaire"""
def strtest(*commentaire):
    print("bonjour {}".format(input(*commentaire)),"")
strtest()
