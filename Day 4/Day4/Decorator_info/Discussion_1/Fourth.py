# we have a solution for this. We can go for "Decorator" function.
# let's write initialization and release 

def decor_function(myfun):  # The 'decor_function' takes a single argument, 'myfun', which is the function to be decorated.
    def with_init_release(): # Within 'decor_function', a nested function called 'with_init_release' is defined.  Inside 'with_init_release', initialization steps are performed before calling myfun, followed by resource release steps after the execution of myfun.
        print("Initialising Resources")
        myfun()
        print("Releasing Resources")
    return with_init_release  # The decorator function returns the 'with_init_release' function, which wraps around the original function myfun.


def fun1():
    print("Important task1")


def fun2():
    print("Important task2")


def fun3():
    print("Important task3")


def fun4():
    print("Important task4") 
    
var1=decor_function(fun1) # This line decorates the fun1 function with the decor_function. Now, var1 holds a reference to the decorated version of fun1, where initialization and release of resources will occur before and after fun1 execution.
var1()   # This line calls the decorated version of fun1, which triggers the initialization, followed by fun1 execution, and finally, the release of resources.
fun2()  # we don't want to do initialization and clean up
var2=decor_function(fun3)
var2()
""" var3=decor_function(fun4)
var3() """
decor_function(fun4)()   # no need to collect function in any variable
                         # This line directly calls the decorated version of fun4, without storing it in a variable

# place breakpoint at all the print statements and at the "return" statement and observe the call stack