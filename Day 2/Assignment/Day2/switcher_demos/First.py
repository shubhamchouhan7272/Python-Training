def myfun(arg):
    switcher = {
        0: "it is zero",
        1: "it is 1",
        2: "it is 2",
      }
    return switcher.get(arg, "invalid number")


print(myfun(1))
print(myfun(5))




