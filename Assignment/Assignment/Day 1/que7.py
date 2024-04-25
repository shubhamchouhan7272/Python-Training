# 7 - Accept numbers till user enters 0 and display the total of all the numbers entered.
def calculate_sum():
    total = 0
    while True:
        num = float(input("Enter a number (enter 0 to finish): "))
        if num == 0:
            break  # Exit the loop if the user enters 0
        total += num
    return total


total_sum = calculate_sum()
print(total_sum)