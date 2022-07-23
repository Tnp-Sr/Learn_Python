#Challenge by Me 1
'''
[Problem] ver 1
P. have a menu to choose to find either area of triangle or rectangle.
====Input==== 
-selected num from the menu
-width
-height
====Output====
-area of selected geometry
'''

#function
def rec(w,h):
    return w * h

def tri(w,h):
    return 0.5 * w * h


#main
print("====Find Area====")
print("select num")
print("[1] rectangle")
print("[2] triangle")
print("=================")

num = int(input("Choose number : "))
w = int(input("\nInput width : "))
h = int(input("Input height : "))

if num > 0 and num <= 2 :
    if num == 1 :
        print("rectangle area = ", rec(w,h))
    elif num == 2 :
        print("triangle area = ", tri(w,h))
else :
    print("!! Wrong Input !!")



