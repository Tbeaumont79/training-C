class Power:
    def __init__(self):
        self.name = "Bod"
        self.age = 20
        self.adress = "Paris"
    def player(self):
        if self.age > 20:
            print("nice tou have {}".format(self.name))

test = Power()
print(test.player())
