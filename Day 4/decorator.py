# Decorator function

"""
def decor_function(myfun):
    def with_init_release():
        print("Installing Resources")
        myfun()
        print("Releasing Resources")
    return with_init_release
def fun1():
    print("Important task1")

def fun2():
    print("Important task2")

def fun3():
    print("Important task3")

def fun4():
    print("Important task4")

var1 = decor_function(fun2)
var1()
"""
# ------------------------------
"""
def decor_function(myfun):
    def with_init_release():
        print("Installing Resources")
        myfun()
        print("Releasing Resources")
    return with_init_release

@decor_function
def fun1():
    print("Important task1")

@decor_function
def fun2():
    print("Important task2")

# @decor_function
def fun3():
    print("Important task3")

# @decor_function
def fun4():
    print("Important task4")

fun1()
fun2()
fun3()
fun4()
"""
# ------------------------------

def main(fun):
    fun()
    print("inside outer function")

def disp():
    print("inside disp function")

main(disp)