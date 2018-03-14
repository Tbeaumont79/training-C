"""AP physique Meca"""
def Euleur(f,a,b,n,y0):
    h = (b-a)/n
    y = [y0]
    l = []
    t = a 
    def f(y):
        return y
    for k in range (0,n-1):
        
        y = y + [y[k] + h*f(y[k],t)]
        t = t + h
        l = y.append()
    print(l)
Euleur(f(5),6,4,100,1)
