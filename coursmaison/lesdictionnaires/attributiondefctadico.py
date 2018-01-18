def fonction_print():
    print("hey yo l'amis")
def reponse_print():
    print("salut à toi")
mon_dico = {}
mon_dico["fonction"] = fonction_print
mon_dico["reponse"] = reponse_print
print(mon_dico["reponse"](),mon_dico["fonction"]())
