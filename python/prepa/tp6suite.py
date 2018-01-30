from random import randrange
def maximum(L):
    M = L[0]
    n = len(L)
    for i in range(1,n):
        if M<=L[i]:
            M = L[i]
            position = [i]
    return(M,position)
L1= [4,5,8,2,4,8,3]
L2= [8,4,5,6,4]
L3 = [2,4,5,1,5,8]
print("l1 =",L1,"à pour maximum",maximum(L1))
print("l2 =",L2,"à pour maximum",maximum(L2))
print("l2 =",L3,"à pour maximum",maximum(L3))
a  = [ randrange(0,41) for i in range(20)]

