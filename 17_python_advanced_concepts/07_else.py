try:
    a = 365 / 0

except Exception as e:
    print(e)

# This will get executed when there is no error in the try block
else:
    print(a)