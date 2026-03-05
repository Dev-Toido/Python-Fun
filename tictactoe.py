import random as r
def check(k):
    boole,t=False,0
    if k[1][1]==k[1][3]==k[1][5] ==' X ':
        boole,t=True,1
    elif k[3][1]==k[3][3]==k[3][5]==' X ':
        boole,t=True,1
    elif k[5][1]==k[5][3]==k[5][5] ==' X ':
        boole,t=True,1
    elif k[1][1]==k[3][1]==k[5][1] ==' X ':
        boole,t=True,1
    elif k[1][3]==k[3][3]==k[5][3] ==' X ':
        boole,t=True,1
    elif k[1][5]==k[3][5]==k[5][5] ==' X ':
        boole,t=True,1
    elif k[1][1]==k[3][3]==k[5][5] ==' X ':
        boole,t=True,1
    elif k[1][5]==k[3][3]==k[5][1] ==' X ':
        boole,t=True,1
    elif k[1][1]==k[1][3]==k[1][5] ==' O ':
        boole,t=True,2
    elif k[3][1]==k[3][3]==k[3][5] ==' O ':
        boole,t=True,2
    elif k[5][1]==k[5][3]==k[5][5] ==' O ':
        boole,t=True,2
    elif k[1][1]==k[3][1]==k[5][1] ==' O ':
        boole,t=True,2
    elif k[1][3]==k[3][3]==k[5][3] ==' O ':
        boole,t=True,2
    elif k[1][5]==k[3][5]==k[5][5] ==' O ':
        boole,t=True,2
    elif k[1][1]==k[3][3]==k[5][5] ==' O ':
        boole,t=True,2
    elif k[1][5]==k[3][3]==k[5][1] ==' O ':
        boole,t=True,2
    return boole,t
def x():
    print('Turn for "X"')
    ch=int(input("Enter your choice (1,2,3,4,5,6,7,8,9)"))
    c={1:'11',2:'13',3:'15',4:'31',5:'33',6:'35',7:'51',8:'53',9:'55'}
    if ch in c:
        ch=c[ch]
        if l[int(ch[0])][int(ch[1])]=='   ':
            l[int(ch[0])][int(ch[1])]=' X '
    else:
        print('Error')
def o():
    print('Turn for "O"')
    ch=int(input("Enter your choice (1,2,3,4,5,6,7,8,9)"))
    c={1:'11',2:'13',3:'15',4:'31',5:'33',6:'35',7:'51',8:'53',9:'55'}
    if ch in c:
        ch=c[ch]
        if l[int(ch[0])][int(ch[1])]=='   ':
            l[int(ch[0])][int(ch[1])]=' O '
    else:
        print('Error')
def nblank():
    if l[1][1]=='   ' or l[1][3]=='   ' or l[1][5]=='   ' or l[3][1]=='   ' or l[3][3]=='   ' or l[3][5]=='   ' or l[5][1]=='   ' or l[5][3]=='   ' or l[5][5]=='   ':
        return False
    else:
        return True
def initial():
    global l
    l1=['+','---','+','---','+','---','+']
    la=['|','   ','|','   ','|','   ','|']
    l3=['+','---','+','---','+','---','+']
    lb=['|','   ','|','   ','|','   ','|']
    l3=['+','---','+','---','+','---','+']
    lc=['|','   ','|','   ','|','   ','|']
    l5=['+','---','+','---','+','---','+']
    l=[l1,la,l3,lb,l3,lc,l5]
def main(fi):
    print('WELCOME TO THE GAME OF TIC TAC TOE !!!')
    print("Player 1 takes 'X' and Player 2 takes 'O'")
    print("The grid numbers are being placed on there places, so choose and place your choice")

    t=[['+---', '+', '---', '+', '---+'], ['| 1 ', '|', ' 2 ', '|', ' 3 |'], ['+---', '+', '---', '+', '---+'], ['| 4 ', '|', ' 5 ', '|', ' 6 |'], ['+---', '+', '---', '+', '---+'], ['| 7 ', '|', ' 8 ', '|', ' 9 |'], ['+---', '+', '---', '+', '---+']]
    
    for i in range(len(l)):
            for j in t[i]:
                print(j,end='')
            print('\t',end='')
            for j in l[i]:
                print(j,end='')
            print()
    while True:
        if check(l)[0]:
            print('Player ',check(l)[1],' wins this game !!! CONGRATULATION!!!')
            break
        if nblank():
            print('Game draw!!!! Play again!!')
            break
        if fi==1:
            x()
            fi=2
        else:
            o()
            fi=1
        for i in range(len(l)):
            for j in t[i]:
                print(j,end='')
            print('\t',end='')
            for j in l[i]:
                print(j,end='')
            print()
l=[]
c=True
fi=r.randint(1,2)
while c:
    initial()
    main(fi)
    if fi==1:
        fi=2
    else:
        fi=1
    t=input('Do you want to continue?(Yes/No)')
    if t.lower() not in 'yes':
        c=False

    
