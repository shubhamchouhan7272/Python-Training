"""
def disp1():
    print("inside display 1")
    return disp2

def disp2():
    print("inside display 2")
    return disp3

def disp3():
    print("inside display 3")

# var1 = disp1()
# var1()
disp1()()()
"""

## inner and outer function

"""
def outer():
    def inner():
        print("inside inner function")
    print("inside outer function")

outer()

"""
# --------------------------------------------
"""
def outer():
    def inner():
        print("inside inner function")
    print("inside outer function")
    return inner

var1 = outer()
var1()
"""
# --------------------------------------------
"""
# Two output parameter
def product(a,b):
    p = a*b
    print(p)

# product(4,5)

# Three output parameter
def product(a,b,c):
    p = a*b*c
    print(p)

# product(4,5,6)
product(4,5,7)
"""
# --------------------------------------------

## function overloading
"""
def disp(*args):
    print("Type of argument : ",type(args))
    # print("Hello Bharat!")
    print("Number of arguments is :",args.__len__())

# disp()
# disp(10)
# disp(20,3,4,5,6)
# disp(7.5,9,True)
disp([10],[20],[30])
"""
# --------------------------------------------
"""
from multipledispatch import dispatch

# passing two parameteras

@dispatch(int,int)
def product(first,second):
    result = first*second
    print(result)

@dispatch(int,int,int)
@dispatch(float,float,float)
def product(first,second,third):
    result = first *second * third
    print(result)

# @dispatch(float,float,float)
# def product(first,second,third):
#     result = first *second * third
#     print(result)

# product(10,23,55) #int
product(1.6,3.4,6.7) #float
"""
# --------------------------------------------

##help [use for show a function's document]

# print("Hello")
# help(print)
# help(str)
# help(int)
# help(object)

# number = input("Enter a number : ")
# print(number)
# print(type(number))
# num2 = int(number)
# print(type(num2))

# print(help(print))

# --------------------------------------------
"""
def my_func(a):
    # function body
    pass

def double(x):
    return x*2

my_list = [1,2,3,4,5,6,7]
new_list = list(map(double, my_list))
print(new_list)   #output = [2, 4, 6, 8, 10, 12, 14]
"""
# --------------------------------------------
