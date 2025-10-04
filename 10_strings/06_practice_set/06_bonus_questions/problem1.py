# Write a program that counts how many vowels are in a given string.

vowels = "a,e,i,o,u"
text = input("Write a sentence: ")
count = 0
text_lower = text.lower()

for char in text_lower:
    if char in vowels:
        print(char)
        count += 1

print(count)