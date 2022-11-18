class Composition:
    def __init__(self):
        self.STORAGE = []

    def __add__(self, val):
        if not val or not isinstance(val, Item):
            return TypeError("You can only add items to storage")
        if val in self.STORAGE:
            return ValueError("Item is already in storage")
        self.STORAGE.append(val)

    def __sub__(self, val):
        if not val or not isinstance(val, Item):
            return TypeError("You can only subtract items from storage")
        if val not in self.STORAGE:
            return ValueError("There's no such item")
        self.STORAGE.remove(val)

    def __str__(self):
        res = "STORAGE\n"
        for item in self.STORAGE:
            res += str(item)
        return res


class Item:
    # STORAGE = []

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

        # self.STORAGE.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name of the item should be a string")
        self.__name = val

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Quantity of the items should be an integer")
        if val <= 0:
            raise ValueError("Quantity of the items should be a positive number")
        self.__quantity = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if not val or not isinstance(val, (int, float)):
            raise TypeError("Price of the items should be an integer or float")
        if val <= 0:
            raise ValueError("Price of the items should be a positive number")
        self.__price = val

    def __iadd__(self, val):
        if self == self.price:
            if not val or not isinstance(val, (int, float)):
                raise TypeError("Price should be integer or float")
            self.__price = self.price + val
        elif self == self.quantity:
            if not val or not isinstance(val, int):
                raise TypeError("Quantity should be integer")
            self.__quantity = self.quantity + val
        elif self == self.name:
            if not val or not isinstance(val, str):
                raise TypeError("Name should be string")
            # val = val.strip()
            # self.__name = self.name + " "
            self.__name = self.name + val
            self.__name = self.name.strip()

    def __isub__(self, val):
        print("__isub__")
        if self == self.price:
            if not val or not isinstance(val, (int, float)):
                raise TypeError("Price should be integer or float")
            self.__price = self.price - val
        elif self == self.quantity:
            if not val or not isinstance(val, int):
                raise TypeError("Quantity should be integer")
            self.__quantity = self.quantity - val
        # elif self == self.name:
        #     if not val or not isinstance(val, str):
        #         raise TypeError("Name should be string")
        #     val = val.strip()
        #     self.__name = self.name.replace(val, '')
        #     self.__name = self.name.strip()
    def __sub__(self, val):
        if isinstance(val, str):
            val = val.strip()
            self.__name = self.name.replace(val, '')
            self.__name = self.name.strip()

    def __str__(self):
        # res = "STORAGE\n"
        # for item in self.STORAGE:
        #     res += f"Item name: {item.name}\n" \
        #            f"Price: {item.price}\n" \
        #            f"Quantity available: {item.quantity}\n"
        # return res
        return f"REPORT:\n" \
               f"Item name: {self.name}\n" \
               f"Price: {self.price}\n" \
               f"Quantity available: {self.quantity}\n"


def main():
    try:
        storage = Composition()

        item1 = Item("Sofa", 20, 17000.5)
        item2 = Item("Fridge", 16, 30700)

        storage + item1
        storage + item2

        # print(item1)
        # print(item2)

        item1.price += 5000
        item1.name += " White comfortable"
        item1 - "comfortable"
        item1.quantity += 5

        item2.price -= 200
        item2.name += " SM-73820LS"
        item2 - "LS"
        item2.quantity -= 2

        # print(item1)
        # print(item2)

        print(storage)

    except ValueError as e:
        print(str(e))

    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()