## python docstring

"""
def square(num):
    '''This function accepts a number and returns the square of the number'''
    return num*num

print(square(10))

# print(square.__doc__) #for returning a ''' ''' line
"""
# print(print.__doc__)

# print(help.__doc__) 

"""
def msg(num):
    '''
    This function accepts a number 
    and print number
    and its type
    and return the square of the number
    '''
    print(num)
    print(type(num))
    return num*num

msg(12)
print(msg.__doc__)
"""

"""
def Add(num1,num2):
    return num1 + num2
print(Add(60,50))
"""

"""
name = input("Enter your name : ")
age = input("Enter your age : ")
print("Your name is : ",name)

print(f"Your name is : {name}")
print("Your name is {} and age is {}".format(name, age))
# print("Your age is {}".format(age))
"""

"""
name = input("Enter your name : ")
age = int(input("Enter your age : "))
messgae = "{}'s age is {}"
print(messgae.format(name,age))

# output

# Enter your name : shubham 
# Enter your age : 22
# shubham's age is 22
"""