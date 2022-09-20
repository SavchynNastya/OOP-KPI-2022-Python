import argparse


def calculate(accum, operator, num):
    if operator == "-":
        return accum - num
    elif operator == "+":
        return accum + num
    elif operator == "":
        return num


def check_if_ebnf(expression):
    if not expression:
        return False, None
    operator = ""
    accumulator = 0
    num = 0
    for ch in expression:
        if ch.isdigit():
            if num is None:
                num = 0
            num = num * 10 + int(ch)
        elif ch in "-+":
            if num is None:
                return False, None
            accumulator = calculate(accumulator, operator, num)
            operator = ch
            num = None
        else:
            return False, None
    return True, calculate(accumulator, operator, num)


def main():
    parser = argparse.ArgumentParser()

    # add positional argument
    parser.add_argument("expression", type=str, nargs='*', default=None)
    args = parser.parse_args()

    try:
        if len(args.expression) > 1:
            raise TypeError
        else:
            print(check_if_ebnf(args.expression))
    except TypeError:
        print("Too many arguments passed, you should enter 1 expression")


if __name__ == "__main__":
    main()

