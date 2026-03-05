import Calender as cal

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
def filegen():
    with open(r"C:\Users\User\AppData\Local\Programs\Python\Python312\Programs\Calendar.txt","w") as obj:
        year=int(input("Enter the calendar's year:- "))
        pcal=cal.calender(year)
        y=yearprint(year)
        for i in y:
            obj.write(" "*43+i+"\n")
        for i in pcal:
            obj.write(i+"\n")
        print("Done!!!")
