import argparse
import operator
import math


def convert_to_float(str_list):
    try:
        numbers = list(map(float, str_list))
        return numbers
    except ValueError:
        print("Wrong value type")


def main():
    parser = argparse.ArgumentParser()

    # add positional arguments
    parser.add_argument("action", type=str, help="What to do with numbers?", nargs='?', default=None)
    parser.add_argument("numbers", type=str, nargs="*", default=None)

    args = parser.parse_args()

    func = ''
    try:
        if not args.action or not args.numbers:
            raise TypeError
        args.numbers = convert_to_float(args.numbers)
        if hasattr(operator, args.action):
            func = getattr(operator, args.action)
            print(func(*args.numbers))
        elif hasattr(math, args.action):
            func = getattr(math, args.action)
            print(func(*args.numbers))
        else:
            raise NameError
    except ValueError:
        print("Impossible to get value")
    except NameError:
        print(f"The function {args.action} is not defined.")
    except TypeError:
        print("Wrong number of arguments")
    except ZeroDivisionError:
        print("Division by zero...")


if __name__ == "__main__":
    main()
