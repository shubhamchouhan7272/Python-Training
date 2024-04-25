# 11 - Accept a number display whether it is prime or not.
def prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        
    return True

number = int(input("Enter a number :- "))
prime(number)