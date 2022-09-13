import argparse


parser = argparse.ArgumentParser()

# add positional argument
parser.add_argument("expression", type=str)


def calculate(accum, operator, num):
    if operator == "-":
        return accum - num
    elif operator == "+":
        return accum + num
    elif operator == "":
        return num


def check_if_ebnf(expression):
    # тут натупила
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


args = parser.parse_args()
print(args)

print(check_if_ebnf(args.expression))
