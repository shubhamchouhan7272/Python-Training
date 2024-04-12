"""
def div(a,b):
    print(a)    #a =4
    print(b)    #b =8
    if (a<b):
        a,b=b,a
        print(a)    #a =8
        print(b)    #a =4
    print(a/b)

div(4,8)    #output =2.0
"""

"""
def div(a,b):
    print(a/b)

def my_div(fun):
    def actual_logic(a,b):
        if a< b:
            a,b = b,a
        return fun(a,b)
    return actual_logic
div1 = my_div(div)
div1(4,8)
"""

