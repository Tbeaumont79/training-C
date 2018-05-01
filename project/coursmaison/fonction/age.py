try:
    a,b = int(input("entrez un nombre pour a : ")),int(input("entrez un nombre pour b : "))

    choix = input("entrez *,-,+ ou / : ")
    if choix == "*":
        result = a*b
        print(result)
    elif choix == "+":
        result = a+b
        print(result)
    elif choix == "/":
        result = a / b
        print(result)
    elif choix == "-":
        result = a-b
        print(result)
except ZeroDivisionError: print("c'est pas jojo ")

