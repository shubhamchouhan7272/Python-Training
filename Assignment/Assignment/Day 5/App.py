# App

from special.Arithmetic import add, multiply, subtract
from special.Display import wish


result_sum = add(5, 3)
result_product = multiply(5, 3)
result_difference = subtract(5, 3)

welcome_message = wish("John")

print("Sum:", result_sum)
print("Product:", result_product)
print("Difference:", result_difference)
print(welcome_message)
