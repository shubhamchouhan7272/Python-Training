# create a package "temp1" inside it create a module "MyModule.py"  

# inside this module create a class "Person" with instance members name and age
# parameterized constructor which accepts "name" and "age"
# __str__ method which displays contents of the object.

# now import this package and module in other python application and instantiate Person class by passing name and age

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"