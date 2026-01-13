words = ["python", "rocks", "ai"]

lengths = [length for word in words if (length := len(word)) >= 4]

print(lengths)  # [6, 5]