def fact(a):
    if a==0:
        return 1
    for i in range(a-1,1,-1):
        a*=i
    return a
def C(n,r):
    return fact(n)//(fact(r)*fact(n-r))
n=10
for i in range(n):
    print("   "*(n-i),end="")
    for j in range(i+1):
        if len(str(C(i,j)))==1:
            print(C(i,j),end="     ")
        elif len(str(C(i,j)))==2:
            print(C(i,j),end="    ")
        elif len(str(C(i,j)))==3:
            print(C(i,j),end="   ")
    print()
