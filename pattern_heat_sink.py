n=10
def oorx(s):
    if len(str(s))>1:
        print(s,end="  ")
    else:
        print(s,end="   ")
for i in range(n):
    for j in range(n,n-i-1,-1):
        oorx(j)
    for j in range(n-i-1,0,-1):
        oorx(n-i)
    for j in range(n-i-1,0,-1):
        oorx(n-i)
    for j in range(n-i+1,n+1,1):
        oorx(j)
    print("\n")
for i in range(n-1):
    for j in range(n,i+1,-1):
        oorx(j)
    for j in range(0,i+1,1):
        oorx(i+2)
    for j in range(0,i+1,1):
        oorx(i+2)
    for j in range(i+3,n+1,1):
        oorx(j)
    print("\n")

