import json
import datetime
import uuid


class Customer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.day = datetime.datetime.now().weekday()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name should be a string")
        self.__name = val

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Surname should be a string")
        self.__surname = val

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Weekday should be an integer")
        if not 0 <= val <= 6:
            raise ValueError("Day should be 0-6")

        days = {0: "Mon", 1: "Tues", 2: "Wed", 3: "Thur", 4: "Fri", 5: "Sat", 6: "Sun"}

        self.__day = days[val]

    def __str__(self):
        return f"{self.name} {self.surname}"


class Monday:
    def __init__(self):
        with open("pizzas.json", "r") as file:
            pizza_data = json.load(file)
        self.day_of_week = "Mon"
        self.name = pizza_data["pizza-of-the-day"][self.day_of_week]["name"]
        self.ingredients = pizza_data["pizza-of-the-day"][self.day_of_week]["ingredients"]
        self.price = pizza_data["pizza-of-the-day"][self.day_of_week]["price"]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name of the pizza must be a string")
        self.__name = val

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, val):
        if not val or not isinstance(val, list):
            raise TypeError("Ingredients of the pizza must be a list")
        if not all(isinstance(item, str) for item in val):
            raise ValueError("Each ingredient should be a string")
        self.__ingredients = val

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        if not val or not isinstance(val, (int, float)):
            raise TypeError("Price of the pizza must be an integer/float")
        if val <= 0:
            raise ValueError("Price must be > 0")
        self.__price = val

    def __str__(self):
        return f"Day of the week: {self.day_of_week}\n"\
               f"Today's pizza: {self.name}\n"


class Tuesday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Tues"


class Wednesday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Wed"


class Thursday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Thur"


class Friday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Fri"


class Saturday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Sat"


class Sunday(Monday):
    def __init__(self):
        super().__init__()
        self.day_of_week = "Sun"


class Order:
    __DAYS = {"Mon": Monday(),
              "Tues": Tuesday(),
              "Wed": Wednesday(),
              "Thur": Thursday(),
              "Fri": Friday(),
              "Sat": Saturday(),
              "Sun": Sunday()}

    def __init__(self, customer, *optional_ing):
        self.id = str(uuid.uuid4())
        self.customer = customer
        self.day = customer.day
        self.optional_ing = optional_ing

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, val):
        if not val or not isinstance(val, Customer):
            raise TypeError("Customer must be an instance of Customer class")
        self.__customer = val

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Day should be a string")
        if not self.__DAYS[val]:
            raise KeyError("There is no such day")
        self.__day = self.__DAYS[val]

    @property
    def optional_ing(self):
        return self.__optional_ing

    @optional_ing.setter
    def optional_ing(self, val):
        if not isinstance(val, (str, tuple)):
            raise TypeError("Ingredients should be a tuple or a string")

        with open("pizzas.json", "r") as file:
            pizza_data = json.load(file)
        if any(ingredient not in pizza_data["optional-ingredients"] for ingredient in val):
            raise KeyError("Sorry, there is no such ingredient to add")
        self.__optional_ing = val

    def form_the_order(self):
        with open("orders.json", "r") as file:
            orders = json.load(file)
        if self.id not in orders:
            orders[self.id] = {}
            orders[self.id]["customer"] = str(self.customer)
            orders[self.id]["name"] = self.day.name
            orders[self.id]["price"] = self.day.price
            orders[self.id]["ingredients"] = self.day.ingredients

        with open("pizzas.json", "r") as file:
            pizza_data = json.load(file)

        additional_price = 0
        orders[self.id]["additional ingredient"] = list()
        for ingredient in self.optional_ing:
            orders[self.id]["additional ingredient"].append(ingredient)
            additional_price += pizza_data["optional-ingredients"][ingredient]

        orders[self.id]["additional price"] = additional_price
        orders[self.id]["summary price"] = additional_price + self.day.price

        with open("orders.json", "w") as file:
            json.dump(orders, file, indent=4)

        return f"CHECK: {self.id}\n"\
               f"Customer: {self.customer}\n"\
               f"Ordered pizza: {self.day.name}\n"\
               f"Added ingredients: {', '.join(self.optional_ing) if self.optional_ing else '---'}\n"\
               f"PRICE: {self.day.price + additional_price}\n"\
               f"Date: {datetime.datetime.now()}\n"


def main():
    try:
        cust1 = Customer("Anthony", "Perkins")
        cust2 = Customer("Maria", "Reynold")

        order1 = Order(cust1, "corn", "bell pepper")
        order2 = Order(cust2)

        print(order1.form_the_order())
        print(order2.form_the_order())

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))
    except KeyError as e:
        print(str(e))


if __name__ == "__main__":
    main()







