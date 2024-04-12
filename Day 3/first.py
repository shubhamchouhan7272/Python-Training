## display method

"""
def display():
    print("first")
    print("second")
    print("third")

display()
"""

"""
def show():
    num1 = 100
    print("The value of num1 is : " +str(num1))
show()
"""

# local variable
"""
var = 500
def display():
    var1 = 300
    global var2
    var2 = 500
    print("value of local variable is : ",var1)
display()

def display1():
    print("Value of var1 is : ",var1)
    print("Value of var2 is : ",var2)
display1()
"""

"""
def disp(var):
    print("inside disp\t",var) #second

def myfun():
    print("inside main") #first
    disp(20)

myfun()
"""

"""
def show(var1,var2):
    print(var1,"\t",var2)

def myfun():
    show("Shubham",30)
myfun()
"""

"""
var = 500
def myfun():
    var = 100
    print("Local variable is\t",var)

"""

"""
var = 500
def fun1():
    print("global var is ",var)
def fun2():
    var=200
    print("global var is ",var)
def fun3():
    global var
    var = 600
    print("global var is ",var)

fun1()
fun2()
fun3() 

# output

# global var is  500
# global var is  200
# global var is  600
"""

"""
def disp(var1,var2=20):
    print(var1,"\t",var2)

def fun():
    disp(10)
    disp(100,200)
fun()

# output

# 10       20
# 100      200
"""

"""
def disp(var1=10,var2=20):
    print(var1,"\t",var2)

def fun():
    disp()
    disp(30)
    disp(100,200)
fun()

# output

# 10       20
# 30       20
# 100      200
"""

"""
def disp(var2,var1=20):
    print(var1,"\t",var2)

def fun():
    disp(30)
fun()

# output

# 20       30
"""


"""
def disp(*vargs):
    print(type(vargs))
    if(vargs.__len__()==0):
        print("no argument passed")
    else:
        for k in vargs:
            print(k)

def fun():
    disp()
    disp(10,20,30)
    disp("abc",200,True,4.7)
fun()

# output


# <class 'tuple'>
# no argument passed
# <class 'tuple'>
# 10
# 20
# 30
# <class 'tuple'>
# abc
# 200
# True
# 4.7
"""


"""
def myfun(**varg):
    print(type(varg))
    for key,value in varg.items():
        print(key,value)

# myfun('A', "hello",5.6,True,500)
myfun(name="Shubham Chouhan",age=24, address = "Dewas" )

# output

# <class 'dict'>
# name Shubham Chouhan
# age 24
# address Dewas
"""



