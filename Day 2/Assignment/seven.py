# accept a character and display whether it is upper case or lower case or not an alphabet. 

char = input("Enter a character : ")

if char.isalpha():
    if char.isupper():
        print(f"The character {char} is in upper case.")
    elif char.islower():
        print(f"The character {char} is in lower case.")
else:
    print(f"The character {char} is not an alphabet")
