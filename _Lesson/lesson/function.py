def get_area(w,h,l):
    if w<0 or h<0 or l<0:
        return 0
    return w*h*l


w=4
h=2
l=4
print(get_area(w,h,l))
print(get_area(w=2,h=-2,l=2))