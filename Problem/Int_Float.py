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
# temp = (dollars + (cents/100)) * cup_cakes
# temp *= 100
# cents = temp % 100
# dollars = temp // 100
# print(str(dollars) + ' ' + str(cents))

print('')
print('# Clock face - 1')
hours2_in = int(input())
min2_in = int(input())
sec2_in = int(input())
mins = (hours2_in*60) + min2_in + (sec2_in/60)
degrees = mins / 6 # 6 degree of clock = 1 mins
print(degrees)


