a=20
s=50
for i in range(s):
    for j in range(s):
        if (i**2+j**2+a**2+2*a*(-i-j))<=0:
            if (i**2+j**2+(a-5)**2+2*(a-5)*(-i-j))<=0:
                print(" ",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
