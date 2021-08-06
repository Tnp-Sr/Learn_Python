import math

print('')
print('# Sum of digits')
# print(n // 10 % 10)
# num1=int(input())
# d1 = n // 100 % 10
# d2 = n // 10 % 10
# d3 = n % 10
# print(d1+d2+d3)


print('')
print('# Fractional part')
# Given a positive real number, print its fractional part.
num2=float(input())
n2_int = math.floor(n)
print(num2-n2_int)
#sol
# x = float(input())
# print(x - int(x))


print('')
print('# Car route')
# A car can cover distance of N kilometers per day.
# How many days will it take to cover a route of length M kilometers?
# The program gets two numbers: N and M.
N = float(input())
M = float(input())
print(math.ceil(M/N))