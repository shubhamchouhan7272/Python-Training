# display fibonicii series of 10 numbers

fibonacci_series = [0,1]

for i in range (2,10):
    next_number = fibonacci_series[-1] + fibonacci_series[-2]
    fibonacci_series.append(next_number)

print("fibonacci series of first 10 numbers : ")
for number in fibonacci_series:
    print(number, end=" ")