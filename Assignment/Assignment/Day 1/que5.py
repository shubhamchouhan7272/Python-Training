# 5 - Accept marks from the user. Using if ...elif ....Else, display whether result is fail, pass, second class, first class, Distintion etc.

num = int(input("Enter the any total percentage :- "))
if num > 33:
    if num >= 80:
        print("Distintion")
    elif num >= 60:
        print("first class")
    else:
        print("second class")
else:
    print("Fail")