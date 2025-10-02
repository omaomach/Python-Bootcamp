a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 2:
        print("You won $2")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")