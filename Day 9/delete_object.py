## delete object


"""
class Sample_class:
    some_variable = 20

    def my_method(self):
        print("Hello my friends")
    
print(Sample_class)         # check if class exists

del Sample_class            # delete the class using del keyword

print(Sample_class)         # check if class exists
"""
# ---------------------------------------------
"""
my_variable1 = 20
my_variable2 = "Hi Bro"

print(my_variable1)
print(my_variable2)

del my_variable1
del my_variable2

print(my_variable1)
print(my_variable2)
"""
# ---------------------------------------------
"""
my_list1 = [1,2,3,4,5,6,7,8,9]
my_list2 = ["Blue","Green","Yellow"]

print(my_list1)
print(my_list2)

# del my_list1[1]

# print(my_list1)

del my_list1[3:5]       #index 3 to 5

print(my_list1)

del my_list2

print(my_list2)
"""
# ---------------------------------------------
"""
my_dict1 = {"small":"big", "black":"white", "up":"down"}
my_dict2 = {"dark":"light", "ice":"water", "sky":"land"}

print(my_dict1)
print(my_dict2)
"""
# ---------------------------------------------
"""
import sys
class MyClass:
    var = 0
    def __init__(self, var) -> None:
        self.var = var
    def getvar(self):
        return self.var
    def __del__(self):
        print("No Reference is left for {}".format(self))

m1 = MyClass(10)
print(sys.getrefcount(m1))
print(hex(id(m1)))
print(m1.getvar())
m2 = m1
print(id(m1))
print(id(m2))
print(hex(id(m1)))
print(m1.getvar())
del m1
print("After deleting m1 ", m2.getvar())
print("done") 
"""
# ---------------------------------------------
"""
import sys
my_list = [1,2,3,4,5,6]

ref_count = sys.getrefcount(my_list)
print(ref_count)
"""
# ---------------------------------------------

class MyClass:
    var = 0
    def __init__(self) -> None:
        pass

m1 = MyClass()
print(m1)