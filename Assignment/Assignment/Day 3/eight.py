# write a function to accept minimum 3 characters and maximum 5 characters. 
# 	[ use default arguments method ]

def length(text, min_length=3, max_length=5):

    return min_length <= len(text) <= max_length

valid_text = input("Enter a text : ")
invalid_text1 = "Hi"
invalid_text2 = "This string is too long."

print(length(valid_text))
print(length(invalid_text1))
print(length(invalid_text2))