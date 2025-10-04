str = "hello world" # Strings are immutable

# name[0] = "N" # You cannot do this, you cannot change a string memory

# a = len(str)
# print(a)
# print(str.upper(), str) # The original string "str" remains intact, its not changed.
# print(str.lower())
# print(str.capitalize())
# print(str.title())

# text = " \njoash omao "
# print(text.strip()) # Output "joash omao"
# print(text.lstrip()) # Output "joash omao "
# print(text.rstrip()) # #Output " joash omao"

# text = "Python is fun"
# print(text.find("is")) # Returns Index if first occurence
# print(text.replace("fun", "awesome"))

# text = "Apples,Bananas,Pineapples"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples']))

text = "omao254"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.isspace())