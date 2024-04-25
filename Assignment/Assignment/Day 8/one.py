# Create a multi-level inheritance , override default constructors in the child classes , instantiate the child class and 
# show how will u invoke parent class constructor from child class ?


class A:
    def __init__(self, name):
        self.name = name
        print("A constructor called")

class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("B constructor called")

class Child(B):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        print("Child constructor called")

child = Child("Alice", 10, "XYZ School")

print("Name:", child.name)
print("Age:", child.age)
print("School:", child.school)
