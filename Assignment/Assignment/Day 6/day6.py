# define a class Employee with
# 	empid,empname and desig
# as instance members 
# parameterized and default constructors
# __str__ method

# create 3 objects with/without passing values and then print their references.

class Employee:
    def __init__(self,empid=0,empname= "Shubham", desig= "NA") -> None:
        self.empid = empid
        self.empname = empname
        self.desig = desig

    def __str__(self) -> str:
        return f"Employee(empid={self.empid}, empname='{self.empname}', desig='{self.desig}')"
    
emp1= Employee()
emp2= Employee(123, "Chouhan", "Engineer")
emp3= Employee(empname="Rohit")

print("Employee 1 reference :", id(emp1))
print("Employee 2 reference :", id(emp2))
print("Employee 3 reference :", id(emp3))