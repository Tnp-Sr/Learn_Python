'''
[Problem]
Sum while <= x. Input x,number(for sum) from user 
'''
#### main
## input
c_num = int(input("Input condition number : "))
## sum loop
sum = 0
i = 0
while sum <= c_num:
    print("number",i+1, end="")
    sum += int(input(" : "))
    print("sum =",sum)
    i += 1
print("---End")