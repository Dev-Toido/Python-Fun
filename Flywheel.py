n=20
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(n-1,i,-1):
        print(" ",end=" ")
    for l in range(n,i,-1):
        print("*",end=" ")
    print()
for i in range(n):
    
    for k in range(n-1,i,-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for l in range(n,i,-1):
        print("*",end=" ")
    print()
