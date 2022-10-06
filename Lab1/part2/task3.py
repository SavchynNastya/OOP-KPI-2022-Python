class Product(object):
    def __init__(self, price, description, qty, **dimensions):
        self.price = price
        self.desc = description
        self.quantity = qty
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @property
    def desc(self):
        return self.__desc

    @property
    def quantity(self):
        return self.__quantity

    @property
    def dimensions(self):
        return self.__dimensions

    @price.setter
    def price(self, val):
        if not isinstance(val, (float, int)):
            raise TypeError("Price must be float value")
        elif val <= 0:
            raise ValueError("Price must be > 0")
        self.__price = val

    @desc.setter
    def desc(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Description must be a string")
        self.__desc = val

    @quantity.setter
    def quantity(self, q):
        if not isinstance(q, int):
            raise TypeError("Quantity must be an integer")
        elif q <= 0:
            raise ValueError("Quantity must be > 0")
        self.__quantity = q

    @dimensions.setter
    def dimensions(self, val):
        if not val or not isinstance(val, dict):
            raise TypeError("Dimensions must be passed as a dict")
        self.__dimensions = val

    def __str__(self):
        return f"Product:\n" \
               f"   Price - {self.price}\n" \
               f"   Description - {self.desc}\n" \
               f"   Quantity - {self.quantity}\n" \
               f"   Dimensions - {self.dimensions}\n"


class Customer:
    def __init__(self, surname, name, patr, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patr
        self.mphone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mphone(self):
        return self.__mphone

    @surname.setter
    def surname(self, val):
        if not isinstance(val, str):
            raise TypeError("Surname must be a string")
        elif len(val) < 2 or any(map(str.isdigit, val)):
            raise ValueError("Surname must be a string without numbers and longer than 2 characters")
        self.__surname = val

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError("Name must be a string")
        elif len(val) < 2 or any(map(str.isdigit, val)):
            raise ValueError("Name must be a string without numbers and longer than 2 characters")
        self.__name = val

    @patronymic.setter
    def patronymic(self, val):
        if not isinstance(val, str):
            raise TypeError("Patronymic must be a string")
        elif len(val) < 2 or any(map(str.isdigit, val)):
            raise ValueError("Patronymic must be a string without numbers and longer than 2 characters")
        self.__patronymic = val

    @mphone.setter
    def mphone(self, val):
        if not isinstance(val, str):
            raise TypeError("Mobile phone must be a string")
        elif len(val) != 10 or not val.isdigit():
            raise ValueError("Mobile phone must be a string of 10 digits")
        self.__mphone = val

    def __str__(self):
        return f"Customer:\n" \
               f"   Surname: {self.surname}   Name: {self.name}\n" \
               f"   Patronymic: {self.patronymic}  Mob. phone: {self.mphone}\n"


class Order:
    def __init__(self, cust, products):
        self.customer = cust
        self.products = products
        self.total = 0.0

    @property
    def customer(self):
        return self.__customer

    @property
    def products(self):
        return self.__products

    @customer.setter
    def customer(self, val):
        if not val:
            raise ValueError("Customer must be passed")
        self.__customer = val

    @products.setter
    def products(self, val):
        if not val or not isinstance(val, list):
            raise ValueError("Products must be passed as a list")
        self.__products = val

    def count_total(self):
        for i in range(len(self.products)):
            self.total += self.products[i].price
        return self.total

    def get_product_info(self):
        return ''.join(list(map(str, self.products)))

    def get_customer_info(self):
        return self.customer

    def __str__(self):
        return f"{self.get_customer_info()}" \
               f"{self.get_product_info()}" \
               f"Total price: {self.count_total()}"


def main():
    customer = Customer("Savchyn", "Anastasiia", "Rostyslavivna", "0968916243")

    product_list = []

    try:
        shirt = Product(60, "White oversize shirt", 3, length=80, width=50)
        tv = Product(1999, "Big TV", 1, length=120, width=15, height=50)
        chair = Product(100, "Comfortable office chair", 2, width=65, height=120)
        product_list.extend([shirt, tv, chair])
    except ValueError as e:
        print(f"Product instance creation is failed: {str(e)}")
    except TypeError as e:
        print(f"Product instance creation is failed: {str(e)}")

    while True:
        try:
            pq = input("Please enter the price and quantity of product('q' to quit): ")
            if pq == 'q' or pq == 'Q':
                break

            price, quantity = pq.split()
            desc = input("Enter the description of product: ")

            length = float(input("Enter the length of product: "))
            width = float(input("Enter the width of product: "))
            height = float(input("Enter the height of product: "))

            prod = Product(float(price), desc, int(quantity), length=length, width=width, height=height)
            product_list.append(prod)

        except ValueError or TypeError as e:
            if "invalid literal for int()" in str(e):
                print("Quantity should be an integer")
            elif "could not convert string to float" in str(e):
                print("Price and dimensions must be numbers")
            else:
                print(str(e))

    if product_list:
        order = Order(customer, product_list)
        print(order)


if __name__ == "__main__":
    main()
