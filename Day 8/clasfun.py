# class function 

"""
class student:
    def __init__(self, name):
        self.__name = name

    def display(self):
        print(self.__name)

s1 = student("Shubham")
# s1.display()
# print(s1.__dict__)
print(dir(s1))
"""
# --------------------------------------------------
"""
class MyClass:
    def __init__(self,num1,num2,num3):
        self.num1 = num1 #public by default
        self._num2 = num2 # protected
        self.__num3 = num3 # private
    
    def getnum1(self):
        return self.num1
    
    def getnum2(self):
        return self._num2
    
    def getnum3(self):
        return self.__num3
    
m1 = MyClass(100,200,300)
print(m1.num1)
print(m1._num2)
# print(m1.__num3)
# print(m1.__dict__)
# print(dir(m1))
print(m1._MyClass__num3)
"""
# --------------------------------------------------
"""
class Test :
    x= 10
    def __init__(self,a,b):
        self.a = a
        self.b = b 

ref = Test
# print(dir(ref))
ref1 = Test
print(id(ref) == id(ref1))

t1 = Test(10,20)        #instance object
t2 = Test(50,60)        #instance object
print(id(t1)==id(t2))
print(dir(t1))
"""
# --------------------------------------------------
"""
class student:
    def __init__(self,name):
        self.name = name

s1 = student("Ram")
print(id(s1))
print(s1.name)
s2 = student("Shyam")
print(id(s2))
print(s2.name)
"""
# --------------------------------------------------

class First:
    var = 20

f1 = First()
f2 = First()

print(First.var)   #highly recommended
print(f1.var)       # not recommended
print("address of var before changing \t", id(f1))
print("address of var before changing \t", id(f2))
print(f2.var)       # not recommended


print("Address of variable before changing \t",id(First.var))
First.var = 50
print("address of variable after changing \t", id(First.var))
print("Value after changing : ")
print(First.var)
print(f1.var)
print(f2.var)