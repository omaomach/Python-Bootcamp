a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# You are entering a number, but python is processing it as a string. If you dont do the transformation to integer when after collecting
# input, you will get an error

sum = a + b
print(sum)