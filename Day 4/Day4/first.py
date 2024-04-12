## using switch ….case   display whether accepted character is vowel or not.


# def check_vowels(var):  ## char = 'A'
#     print(var)
#     vowels = 'aeiouAEIOU'
#     if var in vowels:
#         return True
#     else:
#         return False
    
    
# character = input("Enter a character : ")  # character = 'U'

# if check_vowels(character):
#     print(f"The character '{character}'   is Vowel.")
# else:
#     print(f"The character '{character}'   is not a vowel.")


# def is_vowel(char):
#     print("Value of char is  : ",char)
#     switcher = {
#         'a': True,
#         'e': True,
#         'i': True,
#         'o': True,
#         'u': True,
#         'A': True,
#         'E': True,
#         'I': True,
#         'O': True,
#         'U': True
#     } 
#     return switcher.get(char, False)

# character = input("Enter a character : ")  ## 'S'

# if is_vowel(character):
#     print(f"The charcater '{character} is vowel'")
# else:
#     print(f"The character '{character}' is not a vowel")


## Decorator function

# def fun1():
#     print("Important task1")

# def fun2():
#     print("Important task2")

# def fun3():
#     print("Important task3")

# def fun4():
#     print("Important task4") 

# fun1()
# fun2()
# fun3()
# fun4()



# def fun1():
#     print("Initialising Resources")
#     print("Important task1")
#     print("Releasing Resources")

# def fun2():
#     print("Initialising Resources")
#     print("Important task2")
#     print("Releasing Resources")

# def fun3():
#     print("Initialising Resources")
#     print("Important task3")
#     print("Releasing Resources")

# def fun4():
#     print("Initialising Resources")
#     print("Important task4") 
#     print("Releasing Resources")

# fun1()
# fun2()
# fun3()
# fun4()


# def fun1():
#    # print("Initialising Resources")
#     print("Important task1")
#     print("Releasing Resources")

# def fun2():
#     print("Initialising Resources")
#     print("Important task2")
#  #   print("Releasing Resources")

# def fun3():
#     print("Initialising Resources")
#     print("Important task3")
#  #   print("Releasing Resources")

# def fun4():
#     print("Initialising Resources")
#     print("Important task4") 
#     print("Releasing Resources")

# fun1()
# fun2()
# fun3()
# fun4()

# def decor_function(myfun): 
#     def with_init_release():  
#         print("Initialising Resources")
#         myfun()
#         print("Releasing Resources")
#     return with_init_release 


# def fun1():
#     print("Important task1")
    
# def fun2():
#     print("Important task2")

# def fun3():
#     print("Important task3")

# def fun4():
#     print("Important task4") 
      
# var1 = decor_function(fun2,fun3)
# var1()

# var1 = decor_function(fun3)
# var1()

# fun2()


# decor_function(fun4)()


# def div(a,b):
#     print(a/b)

# def my_div(fun):       
#     def actual_logic(a,b):
#         if a<b:
#             a,b=b,a
#         return fun(a,b)
#     return actual_logic

# div1 = my_div(div) 
# div1(4,8) 


# def decor_function(myfun):
#     def with_init_release():
#         print("Initialising Resources")
#         myfun()
#         print("Releasing Resources")
#     return with_init_release

# @decor_function                 
# def fun1():
#     print("Important task1")

# @decor_function
# def fun2():
#     print("Important task2")


# def fun3():
#     print("Important task3")

# @decor_function
# def fun4():
#     print("Important task4") 
    
# fun1()
# fun2()
# fun3()
# fun4()


# def main(fun): ## fun = disp()
#     fun()
#     print("inside outer function")

# def disp():
#     print("inside disp function")

# main(disp)



