class Employee:
    print()
    # private attribute
    def __init__(self,name,salary,gender):
        self.__name = name 
        self.__salary = salary 
        self.__gender = gender 
    
    #private method
    def _showData(self):
        print('\ndetail')
        print('Name : '+ self.getName())
        print('Salary : ',format(self.getSalary()))
        print('Gender : '+ self.getGender())

    # setter
    def setName(self,name):
        self.__name = name
    def setSalary(self,salary):
        self.__salary = salary
    
    # getter
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getGender(self):
        return self.__gender    
        

print()
emp1 = Employee('Ploy',50000,'female')
emp1.setName('PP')
emp1.setSalary(200000)
print('Name : '+emp1.getName())
print('-------')
emp1._showData()


print()
