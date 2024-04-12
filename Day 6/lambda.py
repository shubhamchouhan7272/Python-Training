
##lambda function

"""
my_list = [1,2,3,4,5,6]

new_list = list(map(lambda x : x*2, my_list))
print(new_list)
"""

"""
disp = lambda:print("welcome")
print("disp is the refrence to the the object of type\t",type(disp))
print("address of the the object where disp refers to is\t",id(disp))
disp()
"""

"""
def myfun(fun):
    fun()
    temp=lambda:print("welcome to lambda world")
    myfun(temp)
"""

"""
disp = lambda x: [print(i) for i in range(1,x)]
myfun(disp,7)
"""

"""
def myfun(*values):
    for i in values:
        print(i)
myfun(10,20,30,40)
"""

"""
myfun1 = lambda*values : [print (i,j) for i,j in values.items()]
myfun1(name="Shubham", address="Dewas", age="24")
"""

"""
def myfun(fun,*val):
    print(type(fun))
    print(type(val))
    fun(val)

multiple= lambda*arg:[print(i) for i in arg]

myfun(multiple,10,20,30,40,50)
"""
