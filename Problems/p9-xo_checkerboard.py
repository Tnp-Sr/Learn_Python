'''
[Problem]
Create a chckerboard from 'o', 'x' (x = brown block, o = white block)
====Input==== 
-width
Ex : 4
====Output====
OXOX
XOXO
OXOX
XOXO

'''
#### main
## input
print("---- XO Checkerboard ----")
round = int(input("Input number of row : "))
## output
for row in range(round):
    for col in range(round):
        ## check col,row
        print("O",end = "") if (row + col) % 2 == 0 else print("X",end = "")  
    print("")
