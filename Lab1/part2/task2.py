from math import gcd


class Rational:
    def __init__(self, num, den):
        # if not isinstance(num, int) or not isinstance(den, int):
        #     raise TypeError("Input should be integer")

        self.__numerator = num
        self.__denominator = den
        self.reduce_fraction()

    def reduce_fraction(self):
        num = self.__numerator
        den = self.__denominator

        d = gcd(num, den)

        num = num // d
        den = den // d

        self.set_values(num, den)

    def set_values(self, num, den):
        if num == 0:
            self.__numerator = 0
            self.__denominator = 1
        elif den == 0:
            raise ZeroDivisionError("Denominator can not be 0")
        else:
            self.__numerator = num
            self.__denominator = den

    def add(self, fr2):
        num = self.__numerator * fr2.__denominator + fr2.__numerator * self.__denominator
        den = self.__denominator * fr2.__denominator
        return Rational(num, den)

    def subtract(self, fr2):
        num = self.__numerator * fr2.__denominator - fr2.__numerator * self.__denominator
        den = self.__denominator * fr2.__denominator
        return Rational(num, den)

    def multiply(self, fr2):
        num = self.__numerator * fr2.__numerator
        den = self.__denominator * fr2.__denominator
        if num < 0 and den < 0:
            num *= -1
            den *= -1
        return Rational(num, den)

    def divide(self, fr2):
        temp = Rational(fr2.__denominator, fr2.__numerator)
        return self.multiply(temp)

    def print_fraction(self):
        print(f"{self.__numerator}/{self.__denominator}")

    def print_to_float_fraction(self):
        print(round((self.__numerator / self.__denominator), 2))

    def print(self):
        self.print_fraction()
        self.print_to_float_fraction()
        # print("\n")


def main():
    try:
        f1 = input("Enter the numerator and denominator for the first fraction:")
        # print(len(f1))

        num1, den1 = f1.split()  # catch an error when more or less than 2 values is passed

        f1 = Rational(int(num1), int(den1))

        f2 = input("Enter the numerator and denominator for the second fraction:")

        num2, den2 = f2.split()
        f2 = Rational(int(num2), int(den2))

        f = f1.add(f2)
        print("Sum: ")
        f.print()

        print("Subtraction: ")
        f = f1.subtract(f2)
        f.print()

        print(f"Multiplication: ")
        f = f1.multiply(f2)
        f.print()

        print(f"Division: ")
        f = f1.divide(f2)
        f.print()

    except ValueError as e:
        if "not enough values to unpack" in str(e):
            print("Not enough arguments entered (should be 2)")
        if "too many values" in str(e):
            print("Too many arguments entered (should be 2)")
        if "invalid literal" in str(e):
            print("You should enter only integers")


if __name__ == "__main__":
    main()
