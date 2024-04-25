# 8 - Accept a character and display whether it is upper case or lower case or not an alphabet.
char = input("Enter the character :- ")
if char.isalpha():
    if char.isupper():
        print("character is uppercase.")
    else:
        print("character is olwercase.")
else:
    print("not a alphabet.")