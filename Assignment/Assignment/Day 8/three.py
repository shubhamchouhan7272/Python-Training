# Go for Hierarchical inheritance, create instances of child class and observe constructor invocation.

class Vehicle:
    def __init__(self) -> None:
        print("Vehicle constructor called")

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("Car constructor called")

class Truck(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("truck constructor called")

car_instance = Car()
truck_instance = Truck()
