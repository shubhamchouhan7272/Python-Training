# define nested function and show how will you invoke it.

def outer():
    
    def inner():
        # This is the nested function.
        print("this message is from inner function.")

    inner()
outer()