# สร้าง class
class Employee:

    print()
    # สร้าง constructor
    def __init__(self):
        pass
    def __init__(self,name,salary,gender):
        self.name = name
        self.salary = salary
        self.gender = gender
    # pass // ให้ทำงานผ่านไปก่อน
    
    # สร้าง method 
    def showData(self):
        print('\ndetail')
        print('Name : '+ str(self.name) )
        print('Salary : {}'.format(self.salary))

    # สร้าง destructor
    def __del__(self):
        print("Bye")

# สร้าง object
print()

emp1 = Employee('Ploy',50000,'female')

emp2 = Employee('Loy',25000,'male')

emp3 = Employee('U',64010,'female')

emp1.showData()
emp2.showData()
emp3.showData()

emp1.salary = 60000
emp1.showData()

print()
