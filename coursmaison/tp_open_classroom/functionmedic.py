#fonction 1 choix du client
from varpharma import *
def medic_choice():
    global Pharma_account
    print(list_medic)
    result = input("choissez votre médicament : 1,2,3,4,5 : ")
    if result == '1':
        print("ok vous avez pris un dolipranne",list_medic[0],
        "cela va vous coutez 5 $ le dolipranne")
        input_quantiti = int(input("combien en voulez vous ?  : "))
        quantiti = list_medic[1] - input_quantiti
        dolipranne_cost = 5 * input_quantiti
        if input_quantiti > list_medic[1]:
            print("On n'a pas assez de dolipranne sorry")
            commandes = input("souhaitez vous les commandés oui / non : ")
            if commandes == "oui" or commandes == "Oui":
                print("trés bien, c'est fait revenez demain :) ")
                commande(quantiti,0,0,0)
                Pharma_account -= dolipranne_cost * 0.5

        dolipranne_cost = 5 * input_quantiti
        print("cela va vous coutez",dolipranne_cost,"$")
        Pharma_account = Pharma_account + dolipranne_cost
    if result == '2':
        print("Ah de bonne vitamine à 9,99 $")
        input_quantiti = int(input("combien de tube voulez vous ? : "))
        quantiti = list_medic[3] - input_quantiti
        vitamine_cost = 9.99 * input_quantiti
        if input_quantiti > list_medic[3]:
            print("Hum, nous en avons que ",list_medic[3]," :s")
            commandes = input("souhaitez vous faire une commande ? : oui/non")
            if commandes == "Oui" or commandes == "oui":
                print("trés bien c'est fait revenez demain")
                commande(0,quantiti,0,0)
                Pharma_account -= vitamine_cost * 0.5
                
        print("cela fera ",vitamine_cost," $")
        Pharma_account = Pharma_account + vitamine_cost
        print("Tres bien vous avez achete",input_quantiti," ",list_medic[2],
        "aurevoir")

    if result == '3':
        print("Trés bon choix ",list_medic[4]," 3$ le smecta ")
        input_quantiti = int(input("combien souhaitez vous en prendre ? : "))
        quantiti = list_medic[5] - input_quantiti
        smecta_cost = 3 * input_quantiti
        if input_quantiti > list_medic[5]:
            print("on en as que ",list_medic[5],"desolé")
            commandes = input("souhaitez vous commandez ? oui/non ")
            if commandes == "oui" or commandes == "Oui":
                print("d'accord je m'en occupe revenez demain")
                commande(0,0,quantiti,0)
                Pharma_account -= smecta_cost * 0.5
        Pharma_account = Pharma_account + smecta_cost
        print("Tres bien vous avez achete",input_quantiti," : "
        ,list_medic[4],"aurevoir")

    if result == '4':
        print("vous avez choisi,",list_medic[6]," cela coute 19,99 $")
        input_quantiti = int(input("combien en voulez vous ? : "))
        quantiti = list_medic[7] - input_quantiti
        antibio_cost = 19.99 * input_quantiti
        if list_medic[7] > input_quantiti:
            print("ont en as que",list_medic[7],"désolé")
            commandes = input("souhaitez vous commandez ? oui/non")
            if commandes == "Oui" or commandes == "oui":
                print("je m'en occupe revenez demain :) ")
                commande(0,0,0,quantiti)
                Pharma_account -= antibio_cost * 0.5 
        print("cela va vous couter",antibio_cost," $ ")
        Pharma_account = Pharma_account + antibio_cost
        print("Tres bien vous avez achete",input_quantiti," : "
        ,list_medic[6],"aurevoir")

            

def commande(dolipranne,vitamine,smecta,antibio):
    list_medic[1] += dolipranne
    list_medic[3] += vitamine
    list_medic[5] += smecta
    list_medic[7] += antibio
medic_choice()
class Ficheclient:
    def __init__(self):
        self.nom = input("quel est votre nom ? : ")
        self.age = input("quel est votre age ? : ")
    

test = Ficheclient()


