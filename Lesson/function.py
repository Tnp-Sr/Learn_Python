def get_area(w,h,l):
    if w<0 or h<0 or l<0:
        return 0
    return w*h*l


w=4
h=2
l=4
print(get_area(w,h,l))
print(get_area(w=2,h=-2,l=2))

# lambda ช่วยให้เขียน function 1 line

clean_text = lambda text : text.strip().capitalize()
first_name = '    LAmbDa'
output_name = clean_text(first_name)
print(output_name)