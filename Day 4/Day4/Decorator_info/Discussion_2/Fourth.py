def div(a,b):
    print(a/b)

def my_div(fun):        # this is the decorator function which takes another function as an argument, invoke it and return it
    def actual_logic(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return actual_logic

div1=my_div(div) 
div1(4,8)  

# place the breakpoints at "print","if",both the "return" statements and observe the call stack
# also observe varibles "a" and "b" inside variables section