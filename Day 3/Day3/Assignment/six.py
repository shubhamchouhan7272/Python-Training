# define a function which accepts a character and return toggle of it.

def toggle_case(char):

    if char.islower():
        return char.upper()
    elif char.isupper():
        return char.lower()
    else:
        return char
    
print(toggle_case(input("Enter a charater : ")))
