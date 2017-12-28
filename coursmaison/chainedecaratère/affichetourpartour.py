import os
chaine = "Salut"
title = "The end"
pause = "systeme pause .."
i = 0

while i < len(chaine):
    print(chaine[i].upper())
    i += 1
    if i == len(chaine):

        print(title.upper().center(10))
