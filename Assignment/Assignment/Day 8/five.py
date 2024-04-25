# create Base class and Sub class with parameterized constructors. Show how will you invoke Base class parameterized constructor from Sub class.

class Base:
    def __init__(self, base_parameter) -> None:
        self.base_parameter = base_parameter
        print("Base class constructor called with parameter :", base_parameter)

class Sub(Base):
    def __init__(self, base_parameter, sub_parameter) -> None:
        super().__init__(base_parameter)
        self.sub_parameter = sub_parameter
        print("Sub class constructor called with parameter:", base_parameter, sub_parameter)

sub_instance = Sub("Base Value", "Sub Value")