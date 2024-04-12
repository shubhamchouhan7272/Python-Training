# var = 100
# print(var)

# del var
# print(var)

"""
class Myclass:
    var = 10
    def __init__(self, var1):
        self.var1 = var1

    def getvar(self):
        return self.var
    
    def __del__(self):              #(__del__) destructor
        print("No reference is left for {}".format(self))

m1 = Myclass(10)
print(id(m1))
print(hex(id(m1)))
print(m1.getvar())
"""
# ---------------------------------------------

# Python program to illustrate destructor
"""
class Employee:

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print('Destructor called, Employee deleted')

obj = Employee()
del obj
"""
# ---------------------------------------------

"""
class Employee:

    def __init__(self) -> None:
        print('Employee created')

    def __del__(self):
        print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
print('Calling Create_obj() funtion...')
obj = Create_obj()
print(obj)
print('Program end..')
"""
# ---------------------------------------------
"""
class A:
    def __init__(self, bb) -> None:
        self.b = bb

class B:
    def __init__(self) -> None:
        self.a = A(self)
    def __del__(self):
        print("die")
def fun():
    b = B()

fun()

## Output
# die

"""
# ---------------------------------------------


