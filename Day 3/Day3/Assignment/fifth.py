# define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.

def check_number(number):

    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0
    
result = check_number(int(input("Enter a number is greater than 0 : ")))
print(result)

result = check_number(-3)
print(result)

result = check_number(0)
print(result)