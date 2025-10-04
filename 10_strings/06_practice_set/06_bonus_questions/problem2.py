# Take a user input string and check if it is a palindrome (same forwards and backwards).

text = input("Write a sentence: ")
text_reverse = text[::-1]

if text == text_reverse:
    print("This text is a palindrome")
else:
    print("This text is not a palindrome")