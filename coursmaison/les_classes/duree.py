"""ce programme a pour but d'intégrer des notions mathématiques dans les classes"""

class Duree:
    def __init__(self, min=0 , sec=0):
        

        self.min = min
        self.sec = sec

    def __str__(self):
        
        return "{0:02} : {1:02}".format(self.min,self.sec)

test = Duree(3,53)
print(test)
