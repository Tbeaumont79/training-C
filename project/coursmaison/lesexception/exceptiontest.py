year = 0
while year != 2000:
    try:
        year = int(input("entrez une anne "))
        if year == 2000:
            print("nice tu as trouver")
            quit()
        print("choose the right year")
        print("do you want to continue or not, yes or no")
        result = input("")
        if result == "yes":
            print("let's continue")
        elif result == "no":
            print("okay see ya")
            quit()
        

        
    except ValueError:
        print("erreur tu aurais du taper un nombre")
        quit()
    except AssertionError:
        pass

