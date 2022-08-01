'''
[Problem]
Build like test case.
====Input==== 
-number
Ex : 3
====Output====
1
12
123

'''


#### main 
## input
print("---- Step nmbers ----")
round = int(input("Input number of round : "))
## output
for row in range(1,round+1):
    for col in range(1,row+1):
        print(col,end = "")
    print("")