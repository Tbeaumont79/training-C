def singleton(classe_definie):
    instances = {}
    def get_instance():
        if classe_definie not in instances:
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]

    return get_instance
@singleton
class test:
    pass

a = test()
b = test()
c = a is b
print(c)
