# 10 - Display prime number from 3 to 30.
for num in range(3, 31):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            break
    else:
        print(num)