from math import gcd, ceil


def reduce(func):
    def wrapped(*args):
        num, den = func(*args)
        if (num < 0 and den < 0) or (num > 0 and den < 0):
            num //= -1
            den //= -1
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
        # if num < 0 and den < 0:
        #     num *= -1
        #     den *= -1
        return num, den

    @reduce
    def __truediv__(self, fr2):
        if not isinstance(fr2, Rational):
            return TypeError("Fraction must be an instance of Rational class")
        num = self.__numerator * fr2.__denominator
        den = self.__denominator * fr2.__numerator
        # if num < 0 and den < 0:
        #     num *= -1
        #     den *= -1
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

    def __str__(self):
        if self.__numerator > self.__denominator > 0 and self.__numerator > 0:
            even_part = self.__numerator // self.__denominator
            new_fr = Rational(self.__numerator, self.__denominator) - Rational(even_part, 1)
            return f"Fraction: {even_part} {new_fr.__numerator if new_fr.__numerator > 0 else -new_fr.__numerator}" \
                   f"/{new_fr.__denominator if new_fr.__denominator > 0 else -new_fr.__denominator}\n" \
                   f"As float: {round((self.__numerator / self.__denominator), 2)}\n"
        elif abs(self.__numerator) > self.__denominator and self.__numerator < 0 or self.__denominator < 0:
            even_part = ceil(self.__numerator / self.__denominator)
            new_fr = Rational(self.__numerator, self.__denominator) - Rational(even_part, 1)
            return f"Fraction: {even_part} {new_fr.__numerator if new_fr.__numerator > 0 else -new_fr.__numerator}" \
                   f"/{new_fr.__denominator if new_fr.__denominator > 0 else -new_fr.__denominator}\n" \
                   f"As float: {round((self.__numerator / self.__denominator), 2)}\n"
        else:
            return f"Fraction: {self.__numerator}/{self.__denominator}\n" \
                   f"As float: {round((self.__numerator / self.__denominator), 2)}\n"


def main():
    try:
        fr1 = Rational(10, 8)
        print(fr1)
        fr2 = Rational(4, 7)
        print(fr2)

        print("--SUM--")
        fr = fr1 + fr2
        print(fr)

        print("--SUBTRACTION--")
        fr = fr1 - fr2
        print(fr)

        print(f"--MULTIPLICATION--")
        fr = fr1 * fr2
        print(fr)

        print(f"--DIVISION--")
        fr = fr1 / fr2
        print(fr)

        print(f"Less than: {fr1 < fr2}")
        print(f"Greater than: {fr1 > fr2}")
        print(f"Less or equal than: {fr1 <= fr2}")
        print(f"Greater or equal than: {fr1 >= fr2}")
        print(f"Equal to: {fr1 == fr2}")

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()
