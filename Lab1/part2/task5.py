MAX_STUDENTS = 20


def show_best_students(grade, name, surname):
    print(f"{grade} - {name} {surname}")


class Group:
    GROUP_LIST = []

    def __init__(self, students):
        for student in students:
            if len(self.GROUP_LIST) < 20:
                self.GROUP_LIST.append(student)

    def find_best_students(self):
        average_grades_list = []

        for student in range(len(self.GROUP_LIST)):
            # print(self.GROUP_LIST[student]._average)
            average_grades_list.append(self.GROUP_LIST[student].average)

        # print(average_grades_list)

        top_grades = []
        for i in range(0, 5):
            max_val = 0

            for j in range(len(average_grades_list)):
                if average_grades_list[j] > max_val:
                    max_val = average_grades_list[j]

            average_grades_list.remove(max_val)
            top_grades.append(max_val)

        # print(top_grades)

        for grade in top_grades:
            for student in range(len(self.GROUP_LIST)):
                if grade == self.GROUP_LIST[student].average:
                    show_best_students(self.GROUP_LIST[student].average,
                                       self.GROUP_LIST[student].name,
                                       self.GROUP_LIST[student].surname)


class Student:
    def __init__(self, name, surname, rec_b, grades):
        self.name = name
        self.surname = surname
        self.record_book = rec_b
        self.grades = grades
        self.average = self.find_average_score()

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book(self):
        return self.__record_book

    @property
    def grades(self):
        return self.__grades

    @name.setter
    def name(self, val):
        # if not isinstance(val, str) or len(val) < 3 or val.isdigit():
        #     raise TypeError("Invalid value entered (should be a string)")
        self.__name = val

    @surname.setter
    def surname(self, val):
        # if not isinstance(val, str) or len(val) < 3 or val.isdigit():
        #     raise TypeError("Invalid value entered (should be a string)")
        self.__surname = val

    @record_book.setter
    def record_book(self, val):
        # if not isinstance(val, str) or len(val) != 5 or val.isalpha():
        #     raise TypeError("Invalid value entered (should be a 5 numbers code)")
        self.__record_book = val

    @grades.setter
    def grades(self, val):
        # if not val:
        #     raise TypeError("Invalid values entered, should be numeric")
        self.__grades = val

    def find_average_score(self):
        grades_len = len(self.__grades)
        sum = 0
        for i in range(grades_len):
            sum += self.__grades[i]
        return sum / grades_len


def main():
    students = []

    s1 = Student("Mary", "Amosova", "14622", [2, 3, 5, 5, 2])
    s2 = Student("Lena", "Peterson", "122", [7, 8, 5, 5, 2])
    s3 = Student("Tony", "Berry", "13922", [2, 3, 5, 5, 3])
    s4 = Student("Sonya", "Light", "102192", [2, 8, 8, 8, 2])
    s5 = Student("Kate", "Smith", "878767", [1, 3, 5, 8, 2])
    s6 = Student("Elizabeth", "Cage", "12322", [7, 3, 5, 5, 9])
    s7 = Student("Anna", "Bett", "1434", [1, 3, 1, 5, 2])

    students.extend([s1, s2, s3, s4, s5, s6, s7])
    while True:
        try:
            name = input("Enter the NAME of student(or 'q' to quit): ")
            if name == 'q':
                break

            if not isinstance(name, str) or len(name) < 3 or name.isdigit():
                raise TypeError("Invalid value entered (should be a string)")
                continue

            surname = input("Enter the SURNAME: ")
            if not isinstance(surname, str) or len(surname) < 3 or surname.isdigit():
                raise TypeError("Invalid value entered (should be a string)")
                continue

            rec_book_num = input("Enter the RECORD BOOK(5 numbers code): ")
            if not isinstance(rec_book_num, str) or len(rec_book_num) != 5 or rec_book_num.isalpha():
                raise TypeError("Invalid value entered (should be a 5 numbers code)")
                continue

            grades = input("Enter at least 5 last GRADES of student: ")
            grades = list(grades.split(" "))
            grades = list(map(float, grades))
            print(grades)

            if not grades:
                raise TypeError("Invalid values entered, should be numeric")
                continue

            s = Student(name, surname, rec_book_num, grades)
            students.append(s)

        except TypeError:
            print("Invalid value entered")
        # except ValueError:
        #     print("I dont know")

        # if not isinstance((name, surname), str):
        #     raise TypeError("Invalid name or surname entered (should be a string)")


    group = Group(students)
    group.find_best_students()


if __name__ == "__main__":
    main()
