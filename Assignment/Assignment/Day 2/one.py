# accept a number and display its table. 

# Accepting input from the user
number = int(input("Enter a number: "))

# Displaying multiplication table
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
