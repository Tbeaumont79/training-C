def obsolete(fonction_origine):
    def fun_modify():
        raise RuntimeError("la fonction {0} est obsolete !".format(fonction_origine))
        return fonction_origine
    return fun_modify

