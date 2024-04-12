# this example shows that module is also an object internally

from importlib.abc import Finder
import First,Second

print(type(First))
print(type(Second))
print(id(First))  # First is the reference to the object of type "class module"
print(id(Second)) # Second is the reference to the object of type "class module"




