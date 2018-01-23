class Helloworld:
    def __init__(self):
        self.name = "bod"
        self.age = 12
        self.hobies = "playing video game"
    def mon_attribut(self):
        print("mon attribut est {0}".format(self.name,self.age,self.hobies))

test = Helloworld()
test.mon_attribut()
a = test.__dict__
print(a)
        
