def rectangle(w,h): # กำหนด function (dynamic typing)
    # code block - เว้นช่องแบ่งส่วน
    area = w*h
    return area
def triangle(w,h): 
    return .5*w*h

w=int(input('width= ')) # รับค่า int
h=int(input("height= ")) # รับค่า float
print(rectangle(w,h))
print(triangle(w,h)) 


