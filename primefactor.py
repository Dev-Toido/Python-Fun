pnos=[]
def prime(n):
    c=0
    for i in range(2,n):
        if not n%i:
            c+=1
    if c==0:
        return True
    else:
        return False
def pfactors(i):
    global pnos
    pf=[]
    if i==1:
        pf.append(1)
    else:
        if prime(i):
            pnos.append(i)
            pf.append(i)
        else:
            k=i
            for a in pnos:
                while k%a==0:
                    pf.append(a)
                    k//=a
    return pf
if __name__=='__main__':
    n=int(input('Enter a no.: '))
    for i in range(1,n+1):
        l=pfactors(i)
        s=str(i)+' = '
        if len(l)==1 and l[0]!=1:
            s+=str(l[0])+' (prime) '
        else:
            l1=[]
            for i in l:
                l1.append(str(i))
            s+='x'.join(l1)
        print(s)

