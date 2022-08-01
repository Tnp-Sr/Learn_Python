'''
[Problem]
Choose a letter and make it to be square.
====Input==== 
-letter 
-width
Ex : x 3
====Output====
xxx
xxx
xxx

'''


#### main
## input
print("---- Square of Letter ----")
letter = input("Input letter : ")
round = int(input("Input number of round : "))
## output
for row in range(round):
    for col in range(round):
        print(letter,end = "")
    print("")
