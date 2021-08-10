import random

atk = random.randint(50, 60)
percent=random.uniform(0,100) # สุ่ม float
if percent<=25.5:
    print('cri')
    atk*=2
print(atk)

moneys=[0,10,50,1000]
money=random.choice(moneys) # choose from list
print(money)
random.shuffle(moneys) # สลับใน list
print(moneys)

