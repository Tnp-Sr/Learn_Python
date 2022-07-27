#### loop

## while
i = 0 # for count round 

while(i<3):
    print("Hello world r :",i+1)
    i += 1
# find sum
start,stop = 1,4
i = start
sum = 0
while(i<stop):
    n = int(input("Input number : "))
    sum += n
    i += 1
print("----sum =",sum)
print("End program")

## For -> know the number of rounds
# for _ in range(start,stop,step):
for i in range(3): # range 0-2
    print("r :",i,"-hello world")
print("----")
for i in range(1,10,2): # range 1-9 step i += 2
    print("r :",i,"-hello world")
# find sum
start,stop = 1,4 # range(1,4) -> 3 rounds
sum = 0
for i in range(start,stop):
    n = int(input("Input number : "))
    sum += n
print("----sum =",sum)
print("End program")

for i in range(1,10): # range(start,final) จน.รอบ = final-start
    if i % 3 == 0 :
        # continue - คำสั่งข้าม
        break # ออก loop
    double = i * 2
    print(double)

## loop in loop
i = 1
while i<=3:
    for j in range(4):
        print("i:",i," j:",j+1)
    print("---")
    i += 1


