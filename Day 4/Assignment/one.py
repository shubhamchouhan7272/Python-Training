#  create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
# invoke caller function by passing show1,show2 and show3

def show1():
    print("This is show 1.")

def show2():
    print("This is show 2.")
    
def show3():
    print("This is show 3.")

def caller(func):
    func()

caller(show1)
caller(show2)
caller(show3)