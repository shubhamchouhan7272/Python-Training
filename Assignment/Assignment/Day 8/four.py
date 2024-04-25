# Create a class "Top1" with "disp1()" method.
# From this class Derive "Bottom1", "Bottom2" and "Bottom3" classes ,override the "disp1()".
# create a function "perform" which can take argument as object of any child class.
# Now show how will u achieve dynamic polymorphism.


class Top1:
    def disp1(self):
        print("Top1 disp1 method")

class Bottom1(Top1):
    def disp1(self):
        print("Bottom1 disp1 method")

class Bottom2(Top1):
    def disp1(self):
        print("Bottom2 disp1 method")

class Bottom3(Top1):
    def disp1(self):
        print("Bottom3 disp1 method")

def perform(obj):
    obj.disp1()

bottom1_obj = Bottom1()
bottom2_obj = Bottom2()
bottom3_obj = Bottom3()

perform(bottom1_obj)
perform(bottom2_obj)
perform(bottom3_obj)