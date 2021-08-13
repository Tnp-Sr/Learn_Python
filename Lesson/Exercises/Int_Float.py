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
# num2=float(input())
# n2_int = math.floor(n)
# print(num2-n2_int)
#sol
# x = float(input())
# print(x - int(x))


print('')
print('# Car route')
# N = float(input())
# M = float(input())
# print(math.ceil(M/N))

print('')
print('# Digital clock')
# min_input=int(input())
# hrs = min_input//60
# mins = min_input % 60
# print(str(hrs) + ' ' + str(mins))

print('')
print('# Total cost')
# dollars = int(input())
# cents = int(input())
# cup_cakes = int(input())
# temp = (dollars + (cents/100)) * cup_cakes # cents -> dollars
# temp *= 100
# cents = temp % 100
# dollars = temp // 100
#sol dollars -> cents
# cost = n * (100 * a + b)
# print(cost // 100, cost % 100)
# print(str(dollars) + ' ' + str(cents))

print('')
print('# Clock face - 1')
# hours2_in = int(input())
# min2_in = int(input())
# sec2_in = int(input())
# degrees = (hours2_in * 30) + (min2_in * 0.5) + (sec2_in * (1/120)) # 1 hour = 30 degrees
#sol
# print(h * 30 + m * 30 / 60 + s * 30 / 3600)
# print(degrees)

print('')
print('# Clock face - 2')
deg_hour = float(input())
deg_min = 12 * (deg_hour % 30)
print(deg_min)
