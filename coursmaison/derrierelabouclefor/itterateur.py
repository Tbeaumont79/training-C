
import os
try:
    def mon_generateur():
        yield 1
        yield 2
        yield 3
    my_iterateur = iter(mon_generateur())
    for nb in my_iterateur:
        print(nb)
        os.system("sleep 1")
except:pass
