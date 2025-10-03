num = int(input(f"Enter a number 1-7: "))

match num:
    case 1:
        print(f"Sunday")
    case 2:
        print(f"Monday")
    case 3:
        print(f"Tuesday")
    case 4:
        print(f"Wednesday")
    case 5:
        print(f"Thursday")
    case 6:
        print(f"Friday")
    case 7:
        print(f"Saturday")
    case _:
        print("Number not 1-7")