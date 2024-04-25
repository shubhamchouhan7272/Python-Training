# display prime numbers from 3 to 30


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Display prime numbers from 3 to 30
print("Prime numbers from 3 to 30:")
for num in range(3, 31):
    if is_prime(num):
        print(num, end=" ")
