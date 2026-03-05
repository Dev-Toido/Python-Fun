"""
Task left
1. Number position placing
2. Ketone group
3. 
"""


def rootw(st):    #To analyse the root word
    D={1: 'meth', 2: 'eth', 3: 'prop', 4: 'but', 5: 'pent', 6: 'hex', 7: 'hept', 8: 'oct', 9: 'non', 10: 'dec'}
    for i in D:
        if st.lower().startswith(D[i]):
            return i,st[len(D[i])::]
def bond(st):        #to analyse the bond type 
    B={'an': 'Single', 'en': 'Double', 'yn': 'Triple'}   
    for i in B:
        if st.lower().startswith(i):
            return B[i],st[len(i)::]
def funal(st):    #to analyse the functional group
    F={'e ': 'Normal', 'ol': 'Alcohol', 'al': 'Aldehyde', 'one': 'Ketone', 'oic acid': 'Carboxylic acid', 'amide': 'Acid amide', 'oyl chloride': 'Acid Chloride', 'amine': 'Amine','enitrile':'Alkyl Cyanides'}
    for i in F:
        if st.lower().startswith(i):
            return F[i]
def modf(l,nf):    #to modify the raw ocprint list according to the functional group
    F={'Alcohol': '-OH', 'Aldehyde': '=O','Carboxylic acid': '-OH', 'Amine': '-NHH', 'Acid Chloride': '-Cl','Acid amide':'-N','Alkyl Cyanides':'≡N'}
    apolo=''
    if nf in F:
        l[2]=l[2][:len(l[2])-2:]+F[nf]
        if nf=='Aldehyde':
            l[3]=l[3][:len(l[3])-2:]+'  '
            l[4]=l[4][:len(l[4])-2:]+'  '
        if nf=='Carboxylic acid'or nf=='Acid Chloride' or nf=='Acid amide':
            l[0]=l[0][:len(l[0])-2:]+'O '
            l[1]=l[1][:len(l[1])-2:]+'ǁ '# chr(449)
            l[3]=l[3][:len(l[3])-2:]+'  '
            l[4]=l[4][:len(l[4])-2:]+'  '
        if nf=='Acid amide':
            l[0]=l[0]+'H '
            l[1]=l[1]+'| '
            l[3]=l[3]+'| '
            l[4]=l[4]+'H '
    elif not nf=="Normal":
        apolo='Sorry Unable to show the compound with functional group '+nf+'!!'
    return l,apolo
def mer(st):    #to combine the rootw, bond, funal functions
    nc,s=rootw(st)
    nb,s=bond(s)
    nf=funal(s)
    return nc,nb,nf
def relead(st,n):    #used to fix the numwords prefix
    if n==1:
        return st
    elif n==2 and st.lower().startswith('di'):
        return st[2::]
    elif n==3 and st.lower().startswith('tri'):
        return st[3::]
    elif n==4 and st.lower().startswith('tetra'):
        return st[5::]
    else:
        return 'Sorry'
def dm(s):    #used to anaylize and give the list of the fuctional group
    l=s.split()
    D=d={}
    for i in l:
        l2=i.split('-')
        l3=l2[0].split(',')
        l2[1]=relead(l2[1],len(l3))
        for j in range(len(l3)):
            l3[j]=int(l3[j])
        d.fromkeys(l3,[l2[1]])
        for i in l3:
            if i in D:
                D[i].append(l2[1])
            else:
                D[i]=[l2[1]]
    return D
def spre(s):    #used to replace the functional group words with symbols
     d=dm(s)
     P={'fluoro': 'F ', 'chloro': 'Cl', 'bromo': 'Br', 'iodo': 'I '}
     for i in d:
         for j in range(len(d[i])):
             if d[i][j].lower() in P:
                 d[i][j]=P[d[i][j].lower()]
     return d

la=['   H ','   | ','H- C -H','   | ','   H ']
le=['   H   H ','   |   | ','H- C = C -H','         ','         ']
ly=['         ','         ','H- C '+chr(8801)+' C -H','         ','         ']
d={'Single':la,'Double':le,'Triple':ly}
st=input('Enter the simple organic compound: ')
D={1: 'meth', 2: 'eth', 3: 'prop', 4: 'but', 5: 'pent', 6: 'hex', 7: 'hept', 8: 'oct', 9: 'non', 10: 'dec'}
ls,s,st,pst=st.lower(),'','',''
for i in D.values():
    if i in ls:
        lit=ls.split(i)
        st=i+lit[1]
        pst=lit[0]
        break
print(st,pst)
    
nc,nb,nf=mer(st+' ')
if nb!='Single'  and nc==1:
    print("NOT AVAILABLE")
else:
        if nb!='Single':
            nc-=1
        l=d[nb]
        dnc=nc
        while dnc>1:
            l[0]=l[0]+'  H '
            l[1]=l[1]+'  | '
            l[2]=l[2][:len(l[2])-1:]+' C -H'
            l[3]=l[3]+'  | '
            l[4]=l[4]+'  H '
            dnc-=1
        l,apolo=modf(l,nf)
        pst=spre(pst)
        check=None
        print(pst)
        if pst!=None:
            for i in pst:
                if len(pst[i])>=2:
                    check=False
                    break
            else:
                check=True
            if check:
                for i in pst:
                    l[0]=l[0][:4*i-1]+pst[i][0]+l[0][4*i+1:]
                    del pst[i][0]
                if pst=={}:
                    for i in pst:
                        l[4]=l[4][:4*i-1]+pst[i][0]+l[4][4*i+1:]
                        del pst[i][0]
        s=''
        for i in l:
            s+=i+'\n'
        print(s)
        print(apolo)
