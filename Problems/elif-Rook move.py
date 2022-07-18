y1=int(input())
x1=int(input())
y2=int(input())
x2=int(input())

if x1==x2:
    if (y1-y2) % 2 == 0: print('YES')
    else : print('NO')
elif y1==y2:
    if (x1-x2) % 2 == 0: print('YES')
    else : print('NO')   
else :
    if (x1-x2) == (y1-y2): print('YES')
    else : print('NO')  