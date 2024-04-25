# accept a number and display whether it is prime or not


def num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Accepting a number from the user
number = int(input("Enter a number: "))

# Checking if the entered number is prime
if num(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
