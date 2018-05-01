T = [1,9,2,3,0,5,6,3,-122,456667,-122321,2122323112323,12222323232323131,23,4]
def swape():
    global T
    swap = True
    while swap == True:
        swap = False
        for i in range(len(T)-1):
            i+=1
            if T[i-1]>T[i]: 
                a = T[i]
                T[i] = T[i-1]  
                T[i-1] = a
                swap = True
                print(T)


swape()
