import argparse
import operator
import math

parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("action", type=str, help="What to do with numbers?")
parser.add_argument("numbers", type=float, nargs="*")

args = parser.parse_args()
# print(args)

func = ''
try:
    if hasattr(operator, args.action):
        func = getattr(operator, args.action)
        print(func(*args.numbers))
    elif hasattr(math, args.action):
        func = getattr(math, args.action)
        print(func(*args.numbers))
    else:
        raise NameError
except NameError:
    print(f"The function {args.action} is not defined.")
except TypeError:
    print("Wrong number of arguments")
except ValueError:
    print("Please, enter an integer of float number")
except ZeroDivisionError:
    print("Division by zero...")
