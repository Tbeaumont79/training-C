import matplotlib.pyplot as plt
import math
#declaration de la fonction f
def f(y,t):
    g = 10
    m = 100
    Lambda = 1
    F = y*y
    y = g - (Lambda/m) * F
    return y 

#fonction permettant de calculer l equation differentielle
def Euler1(f,a,b,y0,n):
#declaration des variables : 
    h=(b-a)/n
    y=[y0]
    t=a
    temps=[a]
    for k in range (0,n+1):
        y=y+[y[k]+h*f(y[k],t)]
        temps=temps+[t]
        t=t+h
     
    return (temps,y)
#tracer de la simulation : 
(t1,y1)=Euler1(f,60,5,1,50);
(t2,y2)=Euler1(f,60,5,1,20);
(t3,y3)=Euler1(f,60,5,1,6);
plt.plot(t1,y1,'o')
plt.plot(t2,y2,'o')
plt.plot(t3,y3,'o')
plt.show()
