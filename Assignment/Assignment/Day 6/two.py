# write object counter program.

class ObjectCounter:
    count = 0

    def __init__(self) -> None:
        ObjectCounter.count +=1
    
    def get_object_count(self):
        return ObjectCounter.count
    
obj1 = ObjectCounter()
obj2 = ObjectCounter()
obj3 = ObjectCounter()

print("Number of object counter : ", obj1.get_object_count())