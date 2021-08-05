subjects = ['Digital', 'Data Com', 'Linear']
print(subjects[0]) # list[index]

subjects[1]='Data Structures'
print(subjects)

subjects.append('Eng Business') # เพิ่มต่อท้าย
print(subjects)

subjects.insert(1,'Data Com') 
print(subjects)

subjects.remove('Eng Business') 
print(subjects)

# tuple คล้าย list แต่ใช้ () แก้ไม่ได้