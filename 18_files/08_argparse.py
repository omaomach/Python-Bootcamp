import argparse

parser = argparse.ArgumentParser(description='Simple Calculator')

parser.add_argument("num1", type=float, help="First number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("operation", choices=["+", "-", "mul", "/"], help="Operation")

args = parser.parse_args()

print(args)

if args.operation == "+":
    print(f"The result is {args.num1 + args.num2}")

elif args.operation == "-":
    print(f"The result is {args.num1 - args.num2}")

elif args.operation == "mul":
    print(f"The result is {args.num1 * args.num2}")

elif args.operation == "/":
    print(f"The result is {args.num1 / args.num2}")

else:
    print("Invalid operation")
