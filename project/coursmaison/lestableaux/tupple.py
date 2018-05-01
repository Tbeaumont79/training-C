mon_tuuple = (0,1,2,3,4)
print(mon_tuuple[2])
def decomposer(entier, divise_par):
    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste
decomposer(25,3)
