def spacest(s,spn,m=0):
    try :
        spn=' '*spn
        assert m in [-1,0,1],-1
        if len(spn)<=len(s):
            return s
        else:
            if m==-1:
                return s+spn[len(s):]

            elif m==1:
                return spn[:len(spn)-len(s)]+s

            elif m==0:
                n=len(spn)-len(s)
                return spn[:n//2]+s+spn[len(s)+n//2:]
    except:
        return s+spn[len(s):]
def cuteprint(llos,m=-1):
    llos=list(llos)
    tlist=[]
    stlist=[]
    nlist=[]
    mainlist=[]
    c=len(llos[0])
    for los in llos:
        if c==len(los):
            tlist.append(list(los))
        else:
            return
    for i in range(c):
        nlist.append(0)
    for i in tlist:
        for j in range(c):
            if len(i[j])>nlist[j]:
                nlist[j]=len(i[j])
    for i in range(len(tlist)):
        for j in range(c):
            if j==0:
                tlist[i][j]="|"+spacest(tlist[i][j],nlist[j]+4,m)+"|"
                if i==0:
                    stlist.append("+"+"-"*(nlist[j]+4)+"+")
            else:
                tlist[i][j]=spacest(tlist[i][j],nlist[j]+4,m)+"|"
                if i==0:
                    stlist.append("-"*(nlist[j]+4)+"+")
        tlist[i][-1]=tlist[i][-1]+"\n"
    stlist[-1]=stlist[-1]+"\n"
    for i in tlist:
        mainlist.append(stlist)
        mainlist.append(i)
    mainlist.append(stlist)
    return mainlist

a=cuteprint((("123","456","7890"),("Hi","Hello","There"),['no','baall','snow']),0)
for i in a:
    for j in i:
        print(j,end="")

            
            
    
