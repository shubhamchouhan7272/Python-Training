"""
class Employee:
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary

e1 = Employee("Ram",10000)
print(e1.name)
print(e1.salary)

e1.salary = 20000
print(e1.salary)
"""

"""
class Employee:
    def __init__(self,name,salary) :
        self.name = name
        self._salary = salary                         # _ means protected = _salary

e1 = Employee("Ram",10000)
print(e1.name)
print(e1._salary)

e1._salary = 30000
print(e1._salary)
"""

class Employee:
    def __init__(self,name,salary) :
        self.__salary = salary

e1 = Employee("Ram",10000)
# print(e1.name)
# print(e1.salary)

print(e1._Employee__name)
print(e1.__Employee__salary)

e1._Employee__salary = 30000
print(e1._Employee__salary)