# accept numbers till user enters 0 and display the total of all the numbers entered.


i = 0
# Accept numbers until the user enters 0
while True:
    num = float(input("Enter a number : "))
    if num == 0:
        break  # Exit the loop if the user enters 0
    i += num
# Display the total sum
print("Total of all numbers entered:", i)
