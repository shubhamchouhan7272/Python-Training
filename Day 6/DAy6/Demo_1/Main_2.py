import First,sys

k=100
print(First)
print(id(First))
print(sys.modules)
print("\n\n\n")
print(globals())
print("Let's delete First")
del First
print(sys.modules)
print("\n\n\n")
print(globals())
