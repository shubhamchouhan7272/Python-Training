# accept marks from the user. Using if…….elif….  Else,  display whether result is 
#  fail, pass, second class , first class, Distinction etc.  


marks = float(input("Enter your marks: "))


if marks < 0 or marks > 100:
    print("Invalid marks! Marks should be between 0 and 100.")
elif marks < 32:
    print("Fail")
elif marks < 33:
    print("Pass")
elif marks < 60:
    print("Second Class")
elif marks < 61:
    print("First Class")
else:
    print("Distinction")
