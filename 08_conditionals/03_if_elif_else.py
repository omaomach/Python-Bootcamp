age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("Lets schedule an interview")
elif(age == 0):
    print("You've just been born")
else:
    print("Sorry you cannot drive")