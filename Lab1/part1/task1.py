import argparse


parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("num1", type=str, help="First number")
parser.add_argument("sign", type=str, help="What to do with numbers?")
parser.add_argument("num2", type=str, help="Second number")

args = parser.parse_args()
# print(args)

try:
    num1 = int(args.num1)
    num2 = int(args.num2)
    if args.sign == '-':
        print(num1 - num2)
    elif args.sign == '+':
        print(num1 + num2)
    elif args.sign == '/':
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("Division by zero...")
    elif args.sign == '*':
        print(num1 * num2)
    else:
        print("Please choose one of arithmetic operations: '+', '-', '*', '/'")
        exit(1)
except ValueError:
    print("You entered not a number")
