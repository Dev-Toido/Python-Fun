n=15

for i in range(60):
    for j in range(60):
        if j in [0,1] and (i in [x for x in range(n)] or i in [x for x in range(n*2,n*3+1)]):
            print("* ",end="")
        elif i in [n-2,n-1,2*n,2*n+1] and j in [x for x in range(2*n)]:
            print("* ",end="")
        elif j in [2*n-2,2*n-1] and (i in [x for x in range(n)] or i in [x for x in range(n*2,n*3+1)]):
            print("* ",end="")
        elif j in [n,n-1] and (i in [x for x in range(n//2-1,2*n)] ):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
