# define a function in such a way that it can accept n number of values and print their sum.

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum(1,2,3,4)
print(result)