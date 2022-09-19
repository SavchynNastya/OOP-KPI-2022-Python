import argparse
import operator

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

parser = argparse.ArgumentParser()

# add positional argument
parser.add_argument("expression", type=str, nargs='*', default=None)

args = parser.parse_args()

try:
    if len(args.expression) == 3:
        num1 = int(args.expression[0])
        oper = args.expression[1]
        num2 = int(args.expression[2])
        print(operators[oper](num1, num2))
    else:
        raise TypeError
except ValueError:
    print("You entered not a number")
except TypeError:
    print("Wrong arguments number")
except KeyError:
    print("Wrong operator entered ('*', '+', '-', '/')")
