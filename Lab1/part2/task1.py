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
        if 0.0 < a < 20.0:
            self.__length = a
        else:
            raise TypeError

    @width.setter
    def width(self, b):
        if 0.0 < b < 20.0:
            self.__width = b
        else:
            raise TypeError

    def perimeter(self):
        return 2 * (self.__width + self.__length)

    def area(self):
        return self.__width * self.__length


def main():
    try:
        a, b = input("Please enter width and length of your rectangle:").split()
        box = Rectangle(float(a), float(b))
        print(f"Perimeter - {box.perimeter()}")
        print(f"Area - {box.area()}")

    except ValueError:
        print("Too many values entered!")
    except TypeError:
        print("You should enter float value (0.0 to 20.0)")


if __name__ == "__main__":
    main()





