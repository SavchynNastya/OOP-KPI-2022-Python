student_data = [
    ["Mary", "Amosova", "14822", [2, 3, 5, 5, 2]],
    ["Lena", "Peterson", "15622", [7, 8, 5, 5, 2]],
    ["Tony", "Berry", "13922", [2, 3, 5, 5, 3]],
    ["Sonya", "Light", "10219", [2, 8, 8, 8, 2]],
    ["Kate", "Smith", "87867", [1, 3, 5, 8, 2]],
    ["Elizabeth", "Cage", "12322", [7, 3, 5, 5, 9]],
    ["Anna", "Bett", "14340", [1, 3, 1, 5, 2]]
]


class Group:
    GROUP_LIST = []

    def __init__(self, students, max_students=20):
        for student in students:
            if len(self.GROUP_LIST) < max_students:
                for i in range(len(self.GROUP_LIST)):
                    if (self.GROUP_LIST[i].name, self.GROUP_LIST[i].surname) == (student.name, student.surname):
                        raise ValueError("Such student in group already exists.")
                self.GROUP_LIST.append(student)

    def find_best_students(self):
        best_results = sorted(self.GROUP_LIST, key=lambda x: x.average, reverse=True)[:5]
        return best_results


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
        if not isinstance(val, str):
            raise TypeError("Invalid NAME entered (should be a string)")
        elif len(val) < 3 or val.isdigit():
            raise ValueError("Invalid NAME entered (should be a string) with more than 3 chars")
        self.__name = val

    @surname.setter
    def surname(self, val):
        if not isinstance(val, str):
            raise TypeError("Invalid SURNAME entered (should be a string)")
        elif len(val) < 3 or val.isdigit():
            raise ValueError("Invalid SURNAME entered (should be a string) with more than 3 chars")
        self.__surname = val

    @record_book.setter
    def record_book(self, val):
        if not isinstance(val, str):
            raise TypeError("Invalid RECORD BOOK entered")
        elif len(val) != 5 or val.isalpha():
            raise ValueError("Invalid RECORD BOOK entered (should be a 5 numbers code)")
        self.__record_book = val

    @grades.setter
    def grades(self, val):
        val = list(map(float, val))
        if not val or len(val) < 5:
            raise ValueError("Invalid GRADES entered, should be numeric")
        self.__grades = val

    def find_average_score(self):
        grades_len = len(self.__grades)
        sum = 0
        for i in range(grades_len):
            sum += self.__grades[i]
        return sum / grades_len


def show_best_students(grade, name, surname):
    return f"{grade} - {name} {surname}"


def main():
    students = []

    for stud in student_data:
        try:
            s = Student(stud[0], stud[1], stud[2], stud[3])
            students.append(s)
        except ValueError as e:
            print(f"Student ({stud[0]} {stud[1]}) instance creation is failed:\n  {str(e)}")
        except TypeError as e:
            print(f"Student ({stud[0]} {stud[1]}) instance creation is failed:\n  {str(e)}")

    while True:
        try:
            name = input("Enter the NAME of student(or 'q' to quit): ")
            if name == 'q' or name == 'Q':
                break

            surname = input("Enter the SURNAME: ")

            rec_book_num = input("Enter the RECORD BOOK(5 numbers code): ")

            grades = input("Enter at least 5 last GRADES of student: ")

            grades = list(grades.split())

            s = Student(name, surname, rec_book_num, grades)
            students.append(s)

        except ValueError or TypeError as e:
            print(str(e))

    try:
        group = Group(students)
        best_students = group.find_best_students()
        for student in best_students:
            print(show_best_students(student.average,
                                     student.name,
                                     student.surname))

    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
