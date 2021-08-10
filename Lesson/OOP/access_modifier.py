class Employee:
    # ชื่อตัวแปร/method - public
    # _ชื่อตัวแปร/method - protected
    # __ชื่อตัวแปร/method - private
    print()
    def __init__(self,name,salary,gender):
        # public attribute
        self._name = name #protected
        self.__salary = salary #private
        self.gender = gender 
    
    #public method
    def showData(self):
        print('\ndetail')
        print('Name : '+ str(self._name) )
        print('Salary : {}'.format(self.__salary))
        print('Gender : {}'.format(self.gender))
        

print()
emp1 = Employee('Ploy',50000,'female')
emp1._name = 'PP'
emp1.showData()

emp2 = Employee('Loy',25000,'male')
emp2.__salary = 60000
emp2.showData()

print()
