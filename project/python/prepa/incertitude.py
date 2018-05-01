""""programme permettant de calculer une incertitude"""
from math import *
import numpy
def incertitude():
    liste = [2,3,4,5,7,3,2,1]
    vmoy =  numpy.mean(liste)#this give use the mean value
    std = sqrt(vmoy(abs(liste[0] - vmoy())**2))
    print(a,std)
incertitude()
    
