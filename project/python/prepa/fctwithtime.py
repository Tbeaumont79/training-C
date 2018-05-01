from math import *
from pylab import *
from matplotlib.pyplot import *
from random import randrange
def drawd():
    figure(1)
    pas = 0.01
    listet = arange(0,2*pi+pas,pas)
    listeX = [(sin(t))**3 for t in listet]
    listeY = [(cos(t)-(cos(t))**4) for t in listet]
    plot(listeX,listeY,color="red")
    title("coeur rouge ")
    show()
n=1000
X = list(range(20))
Y=[0 for k in X]
for k in range(n):
    L=[ randrange(0,41) for i in range(20)]

    i=maxPositionFin(L)[1]
    Y[i]=Y[i]+1

    S=0
for i in X:
    S=S+Y[i]
Ynormed = [float(j)/float(S) for j in Y]

figure(7)
scatter(X,Ynormed,color='red',marker="D")
axis([0,19,0,0.1])
show()

