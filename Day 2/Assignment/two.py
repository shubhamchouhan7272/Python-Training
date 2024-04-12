# using switch ….case   display whether accepted character is vowel or not.
"""
character = input("Please enter a character : ")
character = character.lower()
if character == 'a'or character=='e' or character=='i' or character=='o' or character=='u':
    print(f"{character} is a vowel.")
else :
    print(f"{character} is not a vowel.")
"""

def check_vowels(char): #char = A
    print(char)
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return True
    else:
        return  False
    
character = input("Enter a character : ")

if check_vowels(character):
    print(f"Character '{character}' is a vowel.")
else:
    print(f"Character '{character}' is not a vowel.")