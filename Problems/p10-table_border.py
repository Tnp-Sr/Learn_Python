'''
[Problem]
Create a table border from letter.
====Input==== 
-letter 
-width
Ex : x 4
====Output====
xxxx
x  x
x  x
xxxx

'''

#### main
## input
print("---- Table border ----")
letter = input("Input letter : ")
round = int(input("Input number of round : "))
## output
for row in range(round):
    ## check if first or last row.
    for col in range(round): 
        if row == 0 or row == round-1 or col == 0 or col == round-1:
            print(letter,end = "")
        else : 
                print(" ",end = "")
    print("")
