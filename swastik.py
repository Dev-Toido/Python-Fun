n=20
for i in range(n-2):
    for j in range(i+1):
        if j in [0,1] or i in [n-1,n-2]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for k in range(n-1,i+2,-1):
        print(" ",end=" ")
    for l in range(n,i,-1):
        if l in [n,n-1] or i in [0,1]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("* "*(n*2-2),"* "*(n*2-2),sep="\n")
for i in range(2,n):
    for k in range(n,i+1,-1):
        print(" ",end=" ")
    for j in range(i+1):
        if j in [i-1,i] or i in [n-1,n-2]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i-2):
        print(" ",end=" ")
    for l in range(n,i,-1):
        if l in [i+1,i+2] or i in [0,1]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
