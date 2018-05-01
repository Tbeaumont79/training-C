def time_controller(nb_sec):
    def decorateur(func):
        def func_modify():
            first_time = time.time()
            valeur_renvoyee = func()
            last_time = time.time()
            time_starting = last_time - first_time
            if time_starting >= nb_sec:
                print("la fonction {0} a mis {1} pour demarrer".format(func,time_starting))
            return valeur_renvoyee
        return func
    return decorateur
@time_controller(4)
def wait():
    input("appuyer sur entrée")

wait()
