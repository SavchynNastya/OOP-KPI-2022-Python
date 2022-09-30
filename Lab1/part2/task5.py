MAX_STUDENTS = 20

student_data = [
    ["Mary", "Amosova", "14822", [2, 3, 5, 5, 2]],
    ["Lena", "Peterson", "15622", [7, 8, 5, 5, 2]],
    ["Tony", "Berry", "13922", [2, 3, 5, 5, 3]],
    ["Sonya", "Light", "10219", [2, 8, 8, 8, 2]],
    ["Kate", "Smith", "87867", [1, 3, 5, 8, 2]],
    ["Elizabeth", "Cage", "12322", [7, 3, 5, 5, 9]],
    ["Anna", "Bett", "14340", [1, 3, 1, 5, 2]]
]


def show_best_students(grade, name, surname):
    print(f"{grade} - {name} {surname}")


class Group:
    GROUP_LIST = []

    def __init__(self, students):
        for student in students:
            if len(self.GROUP_LIST) < MAX_STUDENTS:
                self.GROUP_LIST.append(student)

    def find_best_students(self):
        average_grades_list = []

        for student in range(len(self.GROUP_LIST)):
            average_grades_list.append(round(self.GROUP_LIST[student].average, 1))

            # print(average_grades_list)

        top_grades = []
        for i in range(0, 5):
            max_val = 0

            for j in range(len(average_grades_list)):
                if average_grades_list[j] > max_val:
                    max_val = average_grades_list[j]
            # print(max_val)
            average_grades_list.remove(max_val)
            top_grades.append(max_val)

        for grade in top_grades:
            for student in range(len(self.GROUP_LIST)):
                if grade == self.GROUP_LIST[student].average:
                    show_best_students(self.GROUP_LIST[student].average,
                                       self.GROUP_LIST[student].name,
                                       self.GROUP_LIST[student].surname)


class Student:
    __students = []

    def __init__(self, name, surname, rec_b, grades):
        self.name = name
        self.surname = surname
        self.record_book = rec_b
        self.grades = grades
        self.average = self.find_average_score()

        for stud in Student.__students:
            if (stud[0], stud[1]) == (self.surname, self.name):
                raise ValueError("Such student already exists.")
        Student.__students.append([surname, name])

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
        if not isinstance(val, str) or len(val) < 3 or val.isdigit():
            raise ValueError("Invalid NAME entered (should be a string) with more than 3 chars")
        self.__name = val

    @surname.setter
    def surname(self, val):
        if not isinstance(val, str) or len(val) < 3 or val.isdigit():
            raise ValueError("Invalid SURNAME entered (should be a string) with more than 3 chars")
        self.__surname = val

    @record_book.setter
    def record_book(self, val):
        if not isinstance(val, str) or len(val) != 5 or val.isalpha():
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


def main():
    students = []

    for stud in student_data:
        try:
            s = Student(stud[0], stud[1], stud[2], stud[3])
            students.append(s)
        except ValueError as e:
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

        except ValueError as e:
            print(str(e))

    if students:
        group = Group(students)
        group.find_best_students()


if __name__ == "__main__":
    main()
