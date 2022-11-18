from math import gcd


def reduce(func):
    def wrapped(*args):
        num, den = func(*args)
        d = gcd(num, den)
        return Rational(num//d, den//d)
    return wrapped


class Rational:
    def __init__(self, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("You should enter only integers")
        self.__numerator = num
        self.__denominator = den

    def set_values(self, num, den):
        if den == 0:
            raise ZeroDivisionError("Denominator can not be 0")
        self.__numerator, self.__denominator = (0, 1) if num == 0 else (num, den)

    @reduce
    def __add__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        num = self.__numerator * fr2.__denominator + fr2.__numerator * self.__denominator
        den = self.__denominator * fr2.__denominator
        return num, den

    @reduce
    def __sub__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        num = self.__numerator * fr2.__denominator - fr2.__numerator * self.__denominator
        den = self.__denominator * fr2.__denominator
        return num, den

    @reduce
    def __mul__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        num = self.__numerator * fr2.__numerator
        den = self.__denominator * fr2.__denominator
        if num < 0 and den < 0:
            num *= -1
            den *= -1
        return num, den

    @reduce
    def __truediv__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        num = self.__numerator * fr2.__denominator
        den = self.__denominator * fr2.__numerator
        if num < 0 and den < 0:
            num *= -1
            den *= -1
        return num, den

    def __eq__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        return self.__numerator == fr2.__numerator and self.__denominator == fr2.__denominator

    def __le__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        return self.__numerator * fr2.__denominator <= fr2.__numerator * self.__denominator

    def __ge__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        return self.__numerator * fr2.__denominator >= fr2.__numerator * self.__denominator

    def __lt__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        return self.__numerator * fr2.__denominator < fr2.__numerator * self.__denominator

    def __gt__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        return self.__numerator * fr2.__denominator > fr2.__numerator * self.__denominator

    def get_fraction(self):
        return f"{self.__numerator}/{self.__denominator}"

    def get_to_float_fraction(self):
        return f"{round((self.__numerator / self.__denominator), 2)}"

    def print(self):
        print(self.get_fraction())
        print(self.get_to_float_fraction())


def main():
    try:
        fr1 = Rational(5, 8)
        fr2 = Rational(4, 7)

        print("Sum: ")
        fr = fr1 + fr2
        fr.print()

        print("Subtraction: ")
        fr = fr1 - fr2
        fr.print()

        print(f"Multiplication: ")
        fr = fr1 * fr2
        fr.print()

        print(f"Division: ")
        fr = fr1 / fr2
        fr.print()

        print(f"Less than: {fr1 < fr2}")
        print(f"Greater than: {fr1 > fr2}")
        print(f"Less or equal than: {fr1 <= fr2}")
        print(f"Greater or equal than: {fr1 >= fr2}")
        print(f"Equal to: {fr1 == fr2}")

        f1 = input("Enter the numerator and denominator for the first fraction:")

        num1, den1 = f1.split()

        f1 = Rational(int(num1), int(den1))

        f2 = input("Enter the numerator and denominator for the second fraction:")

        num2, den2 = f2.split()
        f2 = Rational(int(num2), int(den2))

        print("Sum: ")
        f = f1 + f2
        f.print()

        print("Subtraction: ")
        f = f1 - f2
        f.print()

        print(f"Multiplication: ")
        f = f1 * f2
        f.print()

        print(f"Division: ")
        f = f1 / f2
        f.print()

    except ValueError as e:
        if "not enough values to unpack" in str(e):
            print("Not enough arguments entered (should be 2)")
        elif "too many values" in str(e):
            print("Too many arguments entered (should be 2)")
        elif "invalid literal" in str(e):
            print("You should enter only integers")
        else:
            print(str(e))
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()
