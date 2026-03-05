import math
L=[]
n=int(input('Enter the value of n -'))
if not n%2:
    for i in range(2,n+1,2):
        l=[] 
        s='  '* ((n-i)//2)+'* '* i
        l.append(s)
        L.append(l)
    for i in range(n,1,-2):
        l=[] 
        s='  '* ((n-i)//2)+'* '* i
        l.append(s)    
        L.append(l)
    for i in L:
        print(i)    
else:
    d=(n//2)* -1
    for i in range(1,n+1):
        ad=int(math.fabs(d))
        l=[]
        s='  '* ad+'* '* (n-ad* 2)
        l.append(s)
        d+=1
        L.append(l)
    for i in L:
        print(i)  
