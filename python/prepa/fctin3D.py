from random import *
import math
from pylab import *
from matplotlib.pyplot import * 
from mpl_toolkits.mplot3d import Axes3D  #librairie permettant de représenter avec 3axes
def projection3d():
    ax = gca(projection='3d')
    ax.set_aspect('equal') #permet de définir une vue « en boite cubique (même cotés) »

    x, y, z = [],[],[]
    for i in range(1000):
        a,b,c = random.gauss(0.0, 1.0), random.gauss(0.0, 1.0), random.gauss(0.0, 1.0)
        length=math.sqrt(a**2 + b**2 + c**2)
        x.append(a/length)
        y.append(b/length)
        z.append(c/length)
    plot(x, y, z, '.') 
    figure(4)

def autreprojection3():
    ax = gca(projection='3d')
    ax.set_aspect('equal')

    listeT = arange(0,10 * pi, 0.1)
    listeX = [cos(t) for t in listeT]
    listeY = [sin(t) for t in listeT]
plot(listeX,listeY)
