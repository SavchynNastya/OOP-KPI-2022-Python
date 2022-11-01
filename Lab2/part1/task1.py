import json
import uuid
import datetime


class Person:
    def __init__(self, name, surname, is_student):
        self.name = name
        self.surname = surname
        self.is_student = is_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Name of a person should be a string")
        self.__name = val

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Surname of a person should be a string")
        self.__surname = val

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, val):
        if not isinstance(val, bool):
            raise TypeError("Student status of a person should be a boolean")
        self.__is_student = val

    def __str__(self):
        return f"{self.name} {self.surname}\n"\
               f"Student status: {self.is_student}"


class RegularTicket:
    def __init__(self, price):
        self.id = uuid.uuid4()
        self.price = price


class Advanced(RegularTicket):
    _ADVANCE_COEF = 0.4  # -40%

    def __init__(self, price):
        super().__init__(price)
        self.price = self.price - self.price * self._ADVANCE_COEF


class Late(RegularTicket):
    _LATE_COEF = 0.1  # +10%

    def __init__(self, price):
        super().__init__(price)
        self.price = self.price + self.price * self._LATE_COEF


class Student(RegularTicket):
    _STUDENT_COEF = 0.5  # -50%

    def __init__(self, price):
        super().__init__(price)
        self.price = self.price - self.price * self._STUDENT_COEF


class Event:

    def __init__(self, hour, day, month, year, price, qty, desc=""):

        self.hour = hour
        self.day = day
        self.month = month
        self.year = year
        self.check_date()

        self.desc = desc
        self.reg_price = price
        self.tickets_quantity = qty

        self.regular_ticket = RegularTicket(self.reg_price)
        self.student_ticket = Student(self.reg_price)
        self.advanced_ticket = Advanced(self.reg_price)
        self.late_ticket = Late(self.reg_price)

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Hour should be an integer")
        if not 0 <= val <= 23:
            raise ValueError("Hour should be 0-23")
        self.__hour = val

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Day should be an integer")
        if not 1 <= val <= 31:
            raise ValueError("Day should be 1-31")
        self.__day = val

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Month should be an integer")
        if not 1 <= val <= 12:
            raise ValueError("Month should be 1-12")
        self.__month = val

    def check_date(self):
        if self.get_datetime(self.year, self.month, self.day, self.hour) < datetime.datetime.now():
            raise ValueError("You can not create event in past")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Year should be an integer")
        if not val >= datetime.date.today().year:
            raise ValueError("Year should be current or higher")
        self.__year = val

    @staticmethod
    def get_datetime(year, month, day, hour):
        return datetime.datetime(year, month, day, hour)

    @property
    def reg_price(self):
        return self.__reg_price

    @reg_price.setter
    def reg_price(self, val):
        if not val or not isinstance(val, (int, float)):
            raise TypeError("Price should be an integer or float")
        if val < 0:
            raise ValueError("Price should be > 0")
        self.__reg_price = val

    @property
    def tickets_quantity(self):
        return self.__tickets_quantity

    @tickets_quantity.setter
    def tickets_quantity(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Tickets quantity should be an integer")
        if val < 0:
            raise ValueError("Tickets quantity should be > 0")
        self.__tickets_quantity = val

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, val):
        if not isinstance(val, str):
            raise TypeError("Description should be a string")
        self.__desc = val

    def ticket_actual_price(self):
        time_to_event = (self.get_datetime(self.year, self.month, self.day, self.hour)
                         - datetime.datetime.now()).days

        if time_to_event < 0:
            return "Sorry, time is up."

        elif time_to_event >= 60:
            return f"You can buy ticket for ADVANCED price: {self.advanced_ticket.price}\n"\
                   f"For students - {self.student_ticket.price}\n"

        elif 0 <= time_to_event <= 10:
            return f"You can buy ticket for LATE price: {self.late_ticket.price}\n" \
                   f"For students - {self.student_ticket.price}\n"

        else:
            return f"You can buy ticket for REGULAR price: {self.regular_ticket.price}\n" \
                   f"For students - {self.student_ticket.price}\n"

    @staticmethod
    def obtain_ticket(ticket, customer, date):
        return f"TICKET: {ticket.id} price: {ticket.price}\n"\
               f"{customer.name} {customer.surname}\n"\
               f"Date: {date}\n"

    def buy_ticket(self, customer):
        if not customer or not isinstance(customer, Person):
            raise TypeError("Customer should be registered")
        if self.tickets_quantity <= 0:
            raise ValueError("Sorry, all the tickets are SOLD OUT!")

        time_to_event = (self.get_datetime(self.year, self.month, self.day, self.hour)
                         - datetime.datetime.now()).days
        if time_to_event <= 0:
            raise TimeoutError("Sorry, there is no time left to this event...")

        self.__tickets_quantity -= 1
        current_time = datetime.datetime.now()

        if customer.is_student:
            ticket = self.student_ticket

        elif time_to_event >= 60:
            ticket = self.advanced_ticket

        elif 0 <= time_to_event <= 10:
            ticket = self.late_ticket

        else:
            ticket = self.regular_ticket

        with open("bought_tickets.json", 'r') as file:
            file_data = json.load(file)

        if "bought_tickets" not in file_data:
            file_data["bought_tickets"] = {}
        if not str(ticket.id) in file_data["bought_tickets"]:
            file_data["bought_tickets"][str(ticket.id)] = {}
            file_data["bought_tickets"][str(ticket.id)]["name"] = customer.name
            file_data["bought_tickets"][str(ticket.id)]["surname"] = customer.surname
            file_data["bought_tickets"][str(ticket.id)]["price"] = ticket.price
            file_data["bought_tickets"][str(ticket.id)]["desc"] = self.desc
            file_data["bought_tickets"][str(ticket.id)]["date"] = str(current_time)

        with open("bought_tickets.json", 'w') as file:
            json.dump(file_data, file, indent=4)

        get_ticket = self.obtain_ticket(ticket, customer, current_time)
        return get_ticket

    @staticmethod
    def search_ticket(ticket_id):
        if not ticket_id or not isinstance(ticket_id, str):
            raise TypeError("Ticket id should be a string")

        with open("bought_tickets.json", 'r') as file:
            file_data = json.load(file)

        if "bought_tickets" not in file_data:
            raise KeyError("There is no tickets bought")

        if ticket_id not in file_data["bought_tickets"]:
            raise KeyError("There is no such ticket bought")

        name = file_data["bought_tickets"][ticket_id]["name"]
        surname = file_data["bought_tickets"][ticket_id]["surname"]
        price = file_data["bought_tickets"][ticket_id]["price"]
        event = file_data["bought_tickets"][ticket_id]["desc"]
        date = file_data["bought_tickets"][ticket_id]["date"]

        return f"\nTICKET: {ticket_id} price: {price}\n" \
               f"EVENT: {event}\n"\
               f"Person: {name} {surname}\n"\
               f"Date: {date}\n"


def main():
    try:
        event1 = Event(16, 30, 11, 2022, 350, 20, "Google Event")
        event2 = Event(12, 6, 3, 2023, 500, 40, "SoftServe Juniors Event")

        print(event1.ticket_actual_price())
        print(event2.ticket_actual_price())

        customer1 = Person("Anna", "Smith", True)
        customer2 = Person("Boris", "Muller", False)

        print(event1.buy_ticket(customer1), sep="\n\n")
        print(event2.buy_ticket(customer2))

        print("Ticket is found:", event1.search_ticket("bee771cc-100b-4731-9761-32c095b75685"))

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))
    except KeyError as e:
        print(str(e))


if __name__ == "__main__":
    main()
