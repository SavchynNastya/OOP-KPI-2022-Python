import argparse
import operator

parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("action", help="What to do with numbers?")
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")

args = parser.parse_args()
# print(args)


# func = None
# get the function from the operator
try:
    func = getattr(operator, args.action)
except AttributeError:
    AttributeError(f"The function {args.action} is not defined.")

# if func:
#     print(func(args.num1, args.num2))
