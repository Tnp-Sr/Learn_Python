'''
[Problem]
Input number until user input number < 0. Find max, min of numbers.
'''

#### function
# max():
# min():

#### main
max = 0
min = 0
check_round = 0
## input
print("----Find Max & Min ----")
while True :
    num = int(input("Input number >= 0 (exit when number < 0) : "))
    if check_round <= 1:
        check_round += 1
    if num < 0:
        break
    ## find max
    if num > max :
        max = num
    ## check if the first round?
    if check_round == 1:
        min = max
    ## findmin
    if num < min : 
        min = num
print("max = ",max,"\nmin = ",min)


## output