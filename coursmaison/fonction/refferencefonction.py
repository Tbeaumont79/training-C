i = 4
"""global i fait appelle a une variable externe à la fonction"""
def variableglobal():
    global i 
    i += 1
    print(i)
variableglobal()
