# create a class "Vehicle", define a method "public void start()" in it. From this class derive a class FourWheeler. 
# How will u override "start()" method of parent class ?


class Vehicle:
    def start(self):
        print("Vehicle started")

class Fourwheeler(Vehicle):
    def start(self):
        print("Four wheeler started")

car = Fourwheeler()
car.start()