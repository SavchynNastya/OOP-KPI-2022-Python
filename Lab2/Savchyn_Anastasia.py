# прізвище, ім'я, по батькові, дата нар., стать
class Person:
    def __init__(self, surname, name, patronymic, birth_date, gender):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.gender = gender

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
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Patronymic should be a string")
        self.__patronymic = val

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Birth date should be a string")
        if not val.split('/') or len(val.split('/')) != 3:
            raise ValueError("You should enter date in such format '12/12/2000'")
        self.__birth_date = val

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Gender should be a string")
        if val != "M" and val != "F":
            raise ValueError("You should enter gender in such format 'M' or 'F'")
        self.__gender = val


# організація, спеціальність за дипломом, посада, оклад, стаж роботи
class Staff(Person):
    def __init__(self, surname, name, patronymic, birth_date, gender,
                 organization, specialty, position, salary, work_experience):
        super().__init__(surname, name, patronymic, birth_date, gender)
        self.organization = organization
        self.specialty = specialty
        self.position = position
        self.salary = salary
        self.work_experience = work_experience

    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Organization should be a string")
        self.__organization = val

    @property
    def specialty(self):
        return self.__specialty

    @specialty.setter
    def specialty(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Specialty should be a string")
        self.__specialty = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if not val or not isinstance(val, str):
            raise TypeError("Position should be a string")
        self.__position = val

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, val):
        if not val or not isinstance(val, (int, float)):
            raise TypeError("Salary should be int or float")
        if val <= 0:
            raise ValueError("Salary should be > 0")
        self.__salary = val

    @property
    def work_experience(self):
        return self.__work_experience

    @work_experience.setter
    def work_experience(self, val):
        if not val or not isinstance(val, (int, float)):
            raise TypeError("Work experience should be int or float")
        if val < 0:
            raise ValueError("Work experience should be >= 0")
        self.__work_experience = val

    def __iadd__(self, val):
        if self == self.salary:
            if not val or not isinstance(val, (int, float)):
                raise TypeError("Salary should be int or float")
            if val <= 0:
                raise ValueError("Salary should be > 0")
            self.__salary = self.salary + val
        elif self == self.work_experience:
            if not val or not isinstance(val, (int, float)):
                raise TypeError("Work experience should be int or float")
            if val < 0:
                raise ValueError("Work experience should be >= 0")
            self.__work_experience = self.work_experience + val
        else:
            raise TypeError("We can not add such values")

    def __lt__(self, other):
        if isinstance(self, Staff) and isinstance(other, Staff):
            return f"Compared by work experience: {self.work_experience < other.work_experience}\n" \
                   f"Compared by salary: {self.salary < other.salary}\n"

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}\n" \
               f"Birth: {self.birth_date}  Gender: {self.gender}\n" \
               f"Specialty: {self.specialty}\n" \
               f"Experience: {self.work_experience} in {self.organization}\n" \
               f"Salary: {self.salary}\n"


# 5. Розробити клас ОРГАНІЗАЦІЯ, що містить послідовнясть об'єктів класу СЛУЖБОВЕЦЬ.
# Знайти кількість осіб, стаж роботи яких перевищує наперед задане значення.
# 6. Для роботи із послідовністю об'єктів побудувати та використати ітератор.
class Organization:
    def __init__(self):
        self.STAFF = []

    def __add__(self, val):
        if not val or not isinstance(val, Staff):
            raise TypeError("You can add only staff to organization")
        if val in self.STAFF:
            raise ValueError("Such worker is already added")
        self.STAFF.append(val)

    def find_by_workexp(self, work_experience):
        if not work_experience or not isinstance(work_experience, (int, float)):
            raise TypeError("Work experience should be int or float")
        if work_experience < 0:
            raise ValueError("Work experience should be >= 0")
        searched_workers = []
        iterator_staff = iter(self)
        for x in iterator_staff:
            if x.work_experience > work_experience:
                searched_workers.append(x)
        return len(searched_workers)

    def __iter__(self):
        return iter(self.STAFF)

    def __len__(self):
        return len(self.STAFF)

    def __next__(self, iter_obj):
        if self.STAFF:
            return next(iter_obj)
        raise StopIteration("StopIteration is raised")


def main():
    try:
        emp1 = Staff("Lymey", "Victoria", "Ivanivna", "23/04/1999", "F",
                     "Soft Serve", "Software Engineer", "Junior", 2000, 1.2)
        emp2 = Staff("Rudyk", "Maria", "Semenivna", "12/04/1995", "F",
                     "Soft Serve", "Software Engineer", "Middle", 3500, 3)
        emp3 = Staff("Tkachenko", "Platon", "Ihorovych", "23/04/2000", "M",
                     "Epam", "Software Engineer", "Junior", 1300, 1)
        emp1.salary += 1200
        print(emp1 < emp3)

        org = Organization()
        org + emp1
        org + emp2
        org + emp3

        print("Workers with experience >1 year quantity: ", org.find_by_workexp(1))

        iterator = iter(org)
        for x in iterator:
            print(x)

    except ValueError as e:
        print(str(e))
    except TypeError as e:
        print(str(e))


if __name__ == "__main__":
    main()