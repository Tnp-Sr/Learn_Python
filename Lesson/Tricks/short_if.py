### short if
#full
time = int(input('Time : '))
if 12 <= time <= 24:
    print("Afternoon")
elif 0 <= time < 12 :
    print("Morning")
else:
    print("Error!")

#short
print('...')
print("Afternoon") if 12 <= time <= 24 else print("Morning") if 0 <= time < 12 else print("Error!")

