import math
L=[]
n=int(input('Enter the value of n -'))
d=(n//2)*-1
for i in range(1,n+1):
    ad=int(math.fabs(d))
    l=[]
    s=' '*ad+'*'*(n-ad*2)
    l.append(s)
    d+=1
    L.append(l)
for i in L:
    for j in i:
        print(j,end='')
    print()    