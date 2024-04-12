import time

i=0
start = time.time()
name = input("Enter your name : ")
age = int(input("Enter your age : "))
message = "Name is {} and Age is {}"
print(message.format(name,age))
print("This program took\t", time.time()-start,"\tseconds")