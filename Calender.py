#Calender
monthsdic={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
def welcome():
    for i in ['  !!!\tW     W  EEEEE  L      CCCCC  OOOOO  M     M  EEEEE  !!! ', ' !!!!!\tW     W  E      L      C   C  O   O  M M M M  E     !!!!!', ' !!!!!\tW  W  W  EEE    L      C      O   O  M  M  M  EEE   !!!!!', '  !!!\tW W W W  E      L      C      O   O  M     M  E      !!! ', '  (.)\t W   W   EEEEE  LLLLL  CCCCC  OOOOO  M     M  EEEEE  (.) ']:
        print('\t'*4+i)


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
def isleap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
def monstru(month,fday=0):#month structure
    global monthsdic
    ml=['+'+'-'*41+'+']#main list
    tdays=0 #total days
    for i in monthsdic:
        if month.lower() in i.lower():
            tdays=monthsdic[i]
            month=i
            break
    a='+-----'*7+'+'
    ml.extend(['|'+spacest(month,41)+'|',a,'| SUN | MON | TUE | WED | THU | FRI | SAT |',a])
    sml=[]#sub main list
    sml=['|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ', '|     ']
    c=1#counter
    for i in range(tdays):
        if i+fday<35:
            if c<10:
                sml[i+fday]="|   "+str(c)+" "
                c+=1
            else:
                sml[i+fday]="|  "+str(c)+" "
                c+=1
        else:
            sml[i+fday-35]="|  "+str(c)+" "
            c+=1
    c,ssml=0,[]#counter,temp string, sub-sub multiple list
    for i in range(5):
        s=''
        for j in range(7):
            s+=sml[c]
            c+=1
        ssml.extend([s+'|',a])
    ml.extend(ssml)
    return ml
def calender(year):
    def ztos(n):#zero to six
        if n<0:
            return n+7
        elif n>6:
            return n-6
        else:
            return n
    global monthsdic
    if isleap(year):
        monthsdic['February']=29
    fwd=1#frist weekday of year
    if year>2024:
        for i in range(2024,year+1):
            if isleap(i):
                fwd+=1
            fwd+=1
            fwd=ztos(fwd)
        fwd-=1
        fwd=ztos(fwd)
    elif year<2024:
        for i in range(2024,year,-1):
            if isleap(i-1):
                fwd-=1
            fwd-=1
            fwd=ztos(fwd)
    sm=[]#super main list
    c=0
    for j in range(4):
        ssm=[]#sub super main list
        for i in range(3):
            mo=list(monthsdic.keys())[c]#month name
            tdays=monthsdic[mo]
            ssm.append(monstru(mo,fwd))
            if fwd+tdays<35:
                fwd=fwd+tdays-28
            else:
                fwd=fwd+tdays-35
            c+=1
        sm.append(ssm)
    pcal=[]#for printing calender
    for j in sm:
        for i in range(15):
            pcal.append(j[0][i]+' '+j[1][i]+' '+j[2][i]+' ')
        pcal[-1]=pcal[-1]+'\n\n'
    return pcal


def yearprint(year):
    didic={0: ['0 0 0 0 0', '0       0', '0       0', '0       0', '0 0 0 0 0'],
       1: ['    1    ', '  1 1    ', '    1    ', '    1    ', '1 1 1 1 1'],
       2: ['2 2 2 2 2', '        2', '2 2 2 2 2', '2        ', '2 2 2 2 2'],
       3: ['3 3 3 3 3', '        3', '3 3 3 3 3', '        3', '3 3 3 3 3'],
       4: ['4       4', '4       4', '4 4 4 4 4', '        4', '        4'],
       5: ['5 5 5 5 5', '5        ', '5 5 5 5 5', '        5', '5 5 5 5 5'],
       6: ['6 6 6 6 6', '6        ', '6 6 6 6 6', '6       6', '6 6 6 6 6'],
       7: ['7 7 7 7 7', '      7  ', '    7    ', '  7      ', '7        '],
       8: ['8 8 8 8 8', '8       8', '8 8 8 8 8', '8       8', '8 8 8 8 8'],
       9: ['9 9 9 9 9', '9       9', '9 9 9 9 9', '        9', '9 9 9 9 9']}
    year=str(year)
    lst=["" for i in range(5)]
    for digit in year:
        for j in range(5):
            lst[j]+=didic[int(digit)][j]+"   "
    return lst


def filegen(year,location=r"C:\Users\User\AppData\Local\Programs\Python\Python312\Programs\Calendar.txt"):
    with open(location,"w") as obj:
        pcal=calender(year)
        y=yearprint(year)
        for i in y:
            obj.write(" "*43+i+"\n")
        for i in pcal:
            obj.write(i+"\n")
        print("Done!!!","with file name Calendar.txt in the location",location)


##main
if __name__=="__main__":
    welcome()
    print('WELCOME TO THE CALENDAR GENERATOR')
    year=int(input("Enter the calendar's year:- "))
    pcal=calender(year)
    y=yearprint(year)
    for i in y:
        print(" "*43+i)
    for i in pcal:
        print(i)
    file=input("Do you want to have a copy of the file as .txt?(yes/no):- ")
    if file.lower()=="yes":
        filegen(year)
