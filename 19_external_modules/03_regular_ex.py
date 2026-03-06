import re

text = "The quick brown fox jumps over the lazy dog. The Brown fox is very cunning!"

# Search for a pattern
# match = re.search("brown", text)
# print(match)
# if match:
#     print("Match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())

# matches = re.findall("brown", text, re.IGNORECASE)
# print("Matches:", matches)

# Replace all occurrences of a pattern
# new_text = re.sub("brown", "blue", text)
# print("New text:", new_text)

# Compile a regex for efficiency (if used multiple times)
pattern = re.compile(r"\b\w+\b") # Matches whole words
words = pattern.findall(text)
print("Words:", words)

# https://regexr.com/