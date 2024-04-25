# create an outer class "Human" with name and gender are the instance members, parameterized constructor and __str__ function
# create an inner class "Register" with username and password.
# also have __str__ function inside it.

# create an object of "Human" and invoke its member function.
# create an object of "Register" and invoke its member function.


class Human:
    def __init__(self,name,gender) -> None:
        self.name = name
        self.gender = gender

    def __str__(self) -> str:
        return f"Human(name='{self.name}', gender='{self.gender}')"

    class Register:
        def __init__(self,username, password) -> None:
            self.username = username
            self.password = password
        
        def __str__(self) -> str:
            return f"Register(username='{self.username}', password='***')"
        
human1 = Human("Shubham", "Male")
print(human1)

register1 = human1.Register("Shubham112","111111")
print(register1)