number = int(input("Enter a number so that I can reverse it: "))
reversed_number = 0 # we create a variable called reversed_number and sets it to 0

while number > 0: # this loop will stop when the number becomes 0 (meaning we have processed all digits), otherwise it will continue as long the number is greater than 0
    digit = number % 10 
    reversed_number = reversed_number * 10 + digit # multiplies current reverse_number by 10 (shifts digits left)
    number = number // 10 # // is integer divisionb (division that rounds down). We are dividing the number by ten to remove the last digit. Example: 123 // 10 = 12, then 12 // 10 = 1, then 1 // 10 = 0

print(f"Reversed number: {reversed_number}")

'''
Full Example with 123:

Start: number = 123, reverse_number = 0
Loop 1: digit = 3, reverse_number = 3, number = 12
Loop 2: digit = 2, reverse_number = 32, number = 1
Loop 3: digit = 1, reverse_number = 321, number = 0
Loop ends (number is 0), prints "Reversed number: 321"

'''