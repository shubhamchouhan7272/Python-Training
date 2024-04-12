# using switch case 

def is_vowel(char):
    switcher = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True,
            'A': True,
            'E': True,
            'I': True,
            'O': True,
            'U': True
    }
    return switcher.get(char, False)

character = input("Enter a character : ")

if is_vowel(character):
    print(f"Character '{character}' is a vowel. ")
else:
    print(f"Character '{character}' is not a vowel. ")