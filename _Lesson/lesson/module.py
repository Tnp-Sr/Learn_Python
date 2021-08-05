# module-แบ่งcodeในไฟล์แยก
def get_rectangle_area(w,h):
    if w<0 or h<0 :
        return 0
    return w*h

def get_triangle_area(w,h):
    if w<0 or h<0 :
        return 0
    return .5*w*h

def get_circle_area(r):
    if r<0:
        return 0
    return (22/7)*(r**2)