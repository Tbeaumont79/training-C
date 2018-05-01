class Temp:
    def __init__(self):
        self.attribut1 = "yo"
        self.attribut2 = "hi"
        self.attribut_tempo = 12

    def __getstat__(self):
        dict_attr__ = dict(self.__dict__)
        dict_attr["attribut temporaire"] = 0
        return dict_attr
test = Temp()


