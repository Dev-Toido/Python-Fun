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
def cbpprint(los0,m=1):
    los=[]
    los1=[]
    
    ch_count=[]
    for i in los0:
        ch_count.append(len(i.strip()))
    space_count=max(ch_count)+4
    for i in los0:
        los.append(spacest(i.strip(),space_count,m))
    for i in range(len(los)):
        los1.append('+---'+'-'*(len(los[i]))+'+\n')
        los[i]='|'+str(i+1)+'. '+los[i]+'|\n'
    llos=[los1[0]]
    for i in range(len(los)):
        llos.append(los[i]+los1[i])
    for i in llos:
        print(i,end='')
    
cbpprint(["ADD NEW RECORD","SEARCH RECORD","DISPLAY ALL RECORDS","DELETE RECORD","MODIFY RECORD","EXIT"],0)    
'''l=eval(input('Enter a List of strings:-> '))
sp=int(input('Enter the no. of space:-> '))
m=int(input('Enter the mode(-1 for left,0 for center,1 for right'))
for i in l:
    print('*',spacest(i,sp,m),'*',sep='')'''
    
