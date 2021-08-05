subjects = ['Digital', 'Data Com', 'Linear']
if 'Digital' in subjects:
    print('WoW!')

if len(subjects)<4:
    subjects.append('Tree Doc')   
print(subjects)

for subject in subjects:
    print(subject)

for i in range(len(subjects)):
    print(str(i+1)+". "+subjects[i])

