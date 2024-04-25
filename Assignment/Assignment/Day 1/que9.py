# 9 - Display fibonici series of 10 number.
a, b = 0, 1
print("Fibonicci series")
for _ in range(10):
    print(a, end =" ")
    a, b = b, a+b