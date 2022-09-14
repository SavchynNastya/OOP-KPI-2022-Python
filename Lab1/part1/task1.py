import argparse

parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("sign", type=str, help="What to do with numbers?")
parser.add_argument("num2", type=int, help="Second number")

args = parser.parse_args()
# print(args)

if args.sign == '-':
    print(args.num1 - args.num2)
elif args.sign == '+':
    print(args.num1 + args.num2)
elif args.sign == '/':
    try:
        print(args.num1 / args.num2)
    except ZeroDivisionError:
        print("Division by zero...")
elif args.sign == '*':
    print(args.num1 * args.num2)
else:
    print("Please choose one of arithmetic operations: '+', '-', '*', '/'")
    exit(1)
