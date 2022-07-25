'''
[Problem]
convert money to Banknote & Coin
Ex:
2000 -> 1000*2
1500 -> 1000*1 + 500*1
1800 -> 1000*1 + 500*1 + 100*3
'''

### Function
def exchangeMoney(m,num):
    dividedMoney = m // num
    m = m % num
    return dividedMoney,m


### main
### ver. no loop
print("--- convert money to Banknote & Coin ---")
m = int(input("Input money : ")) # m = mmoney
bn_1000 = bn_500 = bn_100 = bn_50 = bn_20 = c_10 = c_5 = c_1 = 0

print("> Result [type = number]")
if m <= 0:
    print("Wrong Input")
if m >= 1000:
    bn_1000,m = exchangeMoney(m,1000)
    print("1000 = ",bn_1000)
if m >= 500:
    bn_500,m = exchangeMoney(m,500)
    print("500 = ",bn_500)
if m >= 100:
    bn_100,m = exchangeMoney(m,100)
    print("100 = ",bn_100)
if m >= 50:
    bn_50,m = exchangeMoney(m,50)
    print("50 = ",bn_50)
if m >= 20:
    bn_20,m = exchangeMoney(m,20)
    print("20 = ",bn_20)
if m >= 10:
    c_10,m = exchangeMoney(m,10)
    print("10 = ",c_10)
if m >= 5:
    c_5,m = exchangeMoney(m,5)
    print("5 = ",c_5)
if m >= 1:
    c_1,m = exchangeMoney(m,1)
    print("1 = ",c_1)





