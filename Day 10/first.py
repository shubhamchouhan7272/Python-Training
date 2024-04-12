

"""class First:
    pass

f1=First()
print(type(f1))
"""
# ----------------------------------------------------
# constructor in python
"""
class Student:
    def setName(self,name=None, age=0):
        self.name=name
    def setAge(self,age):
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def __str__(self):              # in order to print object in a readable format
        return self.name+"\t"+str(self.age)

s1=Student()
s1.setName("Shubham")
s1.setAge(24)
print(s1.getName(),"\t",s1.getAge())    

s2=Student()
s2.setName("Rahul")
s2.setAge(35)
print(s2.getName(),"\t",s2.getAge())

s3=Student()
s3.setName("Mohan")
s3.setAge(33)
print(s3.getName(),"\t",s3.getAge())

print("Executing __dict__")
print(s1.__dict__)
print("\n")
print(s1)
# print("Let's print the contents of the class")
# print(dir(Student))
"""
# ----------------------------------------------------
"""
class Employee:
    '''This is the class defined for Employee'''

    name = ""
    design = ""

    def __init__(self,name, design) -> None:
        '''Parametrized constructor in oreder to accept name and design'''
        self.name = name
        self.design = design

    def getName(self):
        '''getter method to get the name'''
        return self.name
    
    def getdesign(self):
        '''getter method to get the designantion'''
        return self.design
    
e1 = Employee("Lieutenant","Shubham")
print(e1.getName())
print(e1.getdesign())
print(e1.__dict__)
print(Employee.__doc__)
print(e1.getName.__doc__)
print(e1.getdesign.__doc__)

"""
# ----------------------------------------------------
"""
class Employee:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

m = Employee("Rohit",24)
print(getattr(m,'name'))
print(getattr(m,'age'))

setattr(m,'name',"Mohit")
setattr(m,'age',29)

print(getattr(m,'name'))
print(getattr(m,'age'))
"""
# ----------------------------------------------------
"""
class Account:
    def __init__(self,name,balance) -> None:
        self.name = name
        self.balance = balance

a1=Account("Monty",50000)
print(getattr(a1,'name'))
print(getattr(a1,'balance'))
"""
# ----------------------------------------------------

