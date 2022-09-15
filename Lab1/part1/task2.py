import argparse
import operator
import math


def convert_to_float(num_str):
    try:
        numbers = list(map(float, num_str))
        return numbers
    except ValueError:
        print("Wrong value type")


parser = argparse.ArgumentParser()

# add positional arguments
parser.add_argument("action", type=str, help="What to do with numbers?")
parser.add_argument("numbers", type=str, nargs="+")

args = parser.parse_args()


# print(args)

func = ''
try:
    args.numbers = convert_to_float(args.numbers)
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
except ZeroDivisionError:
    print("Division by zero...")
