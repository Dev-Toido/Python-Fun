la=['   H ','   | ','H- C -H','   | ','   H ']
le=['   H   H ','   |   | ','H- C = C -H','         ','         ']
ly=['         ','         ','H- C '+chr(8801)+' C -H','         ','         ']
d={1:la,2:le,3:ly}
nc=int(input('Enter the no. of carbon-'))
nb=int(input('Enter the bond type(1,2,3)-'))
if nb>1  and nc==1:
    print("NOT AVAILABLE")
else:
        if nb>1:
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
        for i in l:
            print(i)
