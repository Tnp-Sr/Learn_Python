# try except - หลบการเกิด error ให้ code ทำงานได้
try:
    x = int(input('x = '))
    y = int(input('y = '))
    if x==0:
        raise Exception() # โยนไป exception
    z = x/y
    print(z)
except: # ใน try จะทำงานที่ exception 
    print('Error')

print('Fighting')
