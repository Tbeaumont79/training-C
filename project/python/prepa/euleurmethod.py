import pylab as py
import matplotlib.pyplot as mb
import numpy as np
from math import *
import time
from scipy.integrate import odeint
time1 = time.time()
def euler(ti,tf,h,y0,f):
    a = py.arange(ti,tf,h)
    o = [y0]
    y = y0 #on initialise la suite des images yk
    for k in range(len(a) - 1):
        y = y + h * f(a[k],y)
        o.append(y)
    return(a,o)
time2 = time.time() - time1
ti = 0
tf = 1
y0 = 0.5
h = 0.001
def f1(t,y):
    return(y**2)

T,Y = euler(ti,tf,h,y0,f1)
mb.plot(T,Y)


ti = 0
tf = 5
y0 = 1
def f2(t,y):
    return(y)
time3 = time.time()
h = 1
T1,Y1 = euler(ti,tf,h,y0,f2)
Time3 = time.time() - time3
h = 0.1
T2,Y2 = euler(ti,tf,h,y0,f2)
h = 0.01
T3,Y3 = euler(ti,tf,h,y0,f2)
Yeuler = [exp(k) for k in T3]
mb.plot(T1,Y1,label = "h = 1")
mb.plot(T2,Y2,label = "h = 0.1")
mb.plot(T3,Y3,label = "h = 0.01")
mb.show()
#question 5 : odeint

def f(y,t):
    return(y**2)
ti = 0
tf = 1
y0 = 0.5
h = 0.001
def f(y,t):
    return(y**2)

t = arange(ti,tf,h)
Yodeint = odeint(f,y0,t)








ti = 0
tf = 3
a = 2
b = 0.001
h = 0.01
y0 = [500,1000,2000,3000,5000]
def f(t,y):
    return((a-b*y)*y)

for i in y0:
    T,Y =euler(ti,tf,h,i,f)
    mb.plot(T,Y,label = i)




#question 7
d = 0.05
ti = 0
tf = 50
c = 0.48
b = 0.05
h = 0.0005
y0 = 4
z0 = 10

T = arange(ti,tf,h)
y = [y0]
Z = [z0]
y = y0
z = z0

for n in range(len(T)-1):
    Y,Z = y+k*(a*y-b*y*z),z+h*(-c*z+d*y*z)
    Y.append(y)
    Z.append(z)
mb.plot(T,Z,label="kilolievre")
mb.plot(T,Z,label="linx")
mb.show()





