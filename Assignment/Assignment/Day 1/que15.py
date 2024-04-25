# print the following pattern
# *   *   *   *   *   
#   *   *   *   *   
#     *   *   *   
#       *   *   
#         *  

number_rows = 5

for i in range(number_rows):
    for j in range(number_rows - i - 1):
        print(" ", end="")
    
    for k in range(2 * i + 1):
        print("*", end="")

        print()