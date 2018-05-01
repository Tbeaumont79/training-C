class Bod:

    def __init__(self): 
        self.name = "bod"
        self.age = "haunt"
        self.creation = 2008
        self.level = 100

       
yolo = Bod()
yolo = str(yolo)
def ecriture():

    with open(yolo.name,'w') as f:
        print("voila voila")
def lecture():

    with open(yolo.name,'r') as r:
        print("lecture du fichier en cours : ")
ecriture()
lecture()
