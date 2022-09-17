import argparse
import operator

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("num1", type=str, help="First number", nargs='?', default=None)
parser.add_argument("sign", type=str, help="What to do with numbers?", nargs='?', default=None)
parser.add_argument("num2", type=str, help="Second number", nargs='?', default=None)

args = parser.parse_args()

try:
    num1 = int(args.num1)
    num2 = int(args.num2)
    print(operators[args.sign](num1, num2))
except ValueError:
    print("You entered not a number")
except TypeError:
    print("Wrong argument number")
