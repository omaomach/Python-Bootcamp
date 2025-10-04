'''
Take the string " i love python programming " and:
1. Remove extra spaces from both ends
2. Convert it to title case
3. Count how many times "o" appears
'''

text = " i love python programming "

print(text.strip().title())
print(text.count("o"))

