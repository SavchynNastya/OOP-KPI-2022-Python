class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, a):
        if not isinstance(a, float):
            raise TypeError("You should enter float values")
        elif not 0.0 < a < 20.0:
            raise ValueError("Values must be from 0.0 to 20.0")
        self.__length = a

    @width.setter
    def width(self, b):
        if not isinstance(b, float):
            raise TypeError("You should enter float values")
        elif not 0.0 < b < 20.0:
            raise ValueError("Values must be from 0.0 to 20.0")
        self.__width = b

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def area(self):
        return round(self.__width * self.__length, 2)


def main():
    try:
        box = Rectangle(5.7, 15.3)
        print(f"Perimeter - {box.perimeter()}")
        print(f"Area - {box.area()}")
        a, b = input("Please enter width and length of your rectangle:").split()
        box1 = Rectangle(float(a), float(b))
        print(f"Perimeter - {box1.perimeter()}")
        print(f"Area - {box1.area()}")

    except ValueError as e:
        if "not enough values to unpack" in str(e):
            print("Not enough arguments entered (should be 2)")
        elif "too many values" in str(e):
            print("Too many arguments entered (should be 2)")
        elif "could not convert" in str(e):
            print("You should enter only float values")
        else:
            print(str(e))
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()





