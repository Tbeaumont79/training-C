
"""tracer de groph"""
from math import *
from pylab import *
from matplotlib.pyplot import * 
figure(1)
plot([-10,10], [-19,21])
grid()


"""tracer une courbe y = f(x)"""
figure(2)
title("Ds 3")
pas = 0.01

ListeX = arange(pas, 10, pas)

ListeY = [ x/2  + (1+log(x))/x for x in ListeX ]
ListeY1 = [x/2 + 1 for x in ListeX]
plot(ListeX,ListeY)
plot(ListeX,ListeY1)
grid()
xlabel("fonction f(x) ")
axis([0,10,-5,6])
show()
