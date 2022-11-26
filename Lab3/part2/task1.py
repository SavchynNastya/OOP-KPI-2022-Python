# A software academy teaches two types of courses: local courses
# that are held in some of the academy’s local labs and offsite
# courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a
# course program (sequence of topics). Each teacher has a name
# and knows the courses he or she teaches. Both courses and teachers
# could be printed in human-readable text form. All your courses
# should implement ICourse. Teachers should implement ITeacher.
# Local and offsite courses should implement ILocalCourse and IOffsiteCourse
# respectively. Courses and teachers should be created only through the
# ICourseFactory interface implemented by a class named CourseFactory. Write
# a program that will form courses of software academy.

from abc import ABC, abstractmethod
import sqlite3


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, val):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, val):
        pass

    @property
    @abstractmethod
    def programme(self):
        pass

    @programme.setter
    @abstractmethod
    def programme(self, val):
        pass

    @abstractmethod
    def add_course(self):
        pass


class Course(ICourse):
    def __init__(self, name, teacher, programme):
        self.name = name
        self.teacher = teacher
        self.programme = programme
        self.add_course()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError("Name should be a string")
        self.__name = val

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, val):
        if not isinstance(val, Teacher):
            raise TypeError("Value should be an instance of Teacher class")
        self.__teacher = val

    @property
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, val):
        if not isinstance(val, list):
            raise TypeError("Value should be an instance of Teacher class")
        if not all(isinstance(item, str) for item in val):
            raise ValueError("All values in list should be strings")
        self.__programme = val

    def add_course(self):
        db_connection = sqlite3.connect('coursefactory.db')
        cursor = db_connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='courses' ")
        if cursor.fetchone()[0] == 0:
            create_table = "CREATE TABLE courses (" \
                           "id INTEGER PRIMARY KEY NOT NULL, " \
                           "name TEXT NOT NULL," \
                           "teacher TEXT NOT NULL, " \
                           "programme TEXT NOT NULL );"
            cursor.execute(create_table)
            db_connection.commit()

        get_last_id = "SELECT MAX(id) FROM courses"
        cursor.execute(get_last_id)
        last_id = cursor.fetchone()[0]
        if not last_id:
            last_id = 0

        cursor.execute("SELECT id FROM courses WHERE name=?", (self.name, ))
        id = cursor.fetchone()
        if id:
            # raise ValueError("Such course already exist")
            return "Such course already exist"



        add_to_table = "INSERT INTO courses VALUES " \
                       "(?, ?, ?, ?)"
        cursor.execute(add_to_table, (last_id+1, self.name, self.teacher.name, ', '.join(self.programme)))
        db_connection.commit()

        cursor.close()

    def __str__(self):
        db_connection = sqlite3.connect('coursefactory.db')
        cursor = db_connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='courses' ")
        if cursor.fetchone()[0] == 0:
            # raise ValueError("There is no courses added yet")
            return "There is no courses added yet"
        cursor.execute("SELECT name, teacher, programme FROM courses WHERE name=?",
                       (self.name, ))
        course = cursor.fetchone()
        cursor.close()
        return f"COURSE -{course[0]}-\n" \
               f"Teacher - {course[1]}\n" \
               f"Programme - {course[2]}\n"


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def lab(self):
        pass

    @lab.setter
    @abstractmethod
    def lab(self, val):
        pass


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name, teacher, programme, lab):
        super().__init__(name, teacher, programme)
        self.lab = lab

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, val):
        if not isinstance(val, str):
            raise TypeError("Laboratory name should be a string")
        self.__lab = val


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def place(self):
        pass

    @place.setter
    @abstractmethod
    def place(self, val):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name, teacher, programme, place):
        super().__init__(name, teacher, programme)
        self.place = place

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, val):
        if not isinstance(val, str):
            raise TypeError("Laboratory name should be a string")
        self.__place = val


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, val):
        pass

    @abstractmethod
    def add_teacher(self):
        pass

    @abstractmethod
    def get_courses(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name
        self.add_teacher()
        self.get_courses()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        if not isinstance(val, str):
            raise TypeError("Name should be a string")
        if len(val.split()) != 3:
            raise ValueError("Wrong format! Should be surname, name, patronymic")
        self.__name = val

    def add_teacher(self):
        db_connection = sqlite3.connect('coursefactory.db')
        cursor = db_connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='teachers' ")
        if cursor.fetchone()[0] == 0:
            create_table = "CREATE TABLE teachers (" \
                           "id INTEGER PRIMARY KEY NOT NULL, " \
                           "name TEXT NOT NULL );"
            cursor.execute(create_table)
            db_connection.commit()

        get_last_id = "SELECT MAX(id) FROM teachers"
        cursor.execute(get_last_id)
        last_id = cursor.fetchone()[0]
        if not last_id:
            last_id = 0

        cursor.execute("SELECT id FROM teachers WHERE name=?", (self.name,))
        id = cursor.fetchone()
        if id:
            # raise ValueError("Such teacher already exist")
            return "Such teacher already exist"

        cursor.execute("INSERT INTO teachers VALUES(?, ?)", (last_id+1, self.name))
        db_connection.commit()

        cursor.close()

    def get_courses(self):
        db_connection = sqlite3.connect('coursefactory.db')
        cursor = db_connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='courses' ")
        if cursor.fetchone()[0] == 0:
            return f"{self.name} has no courses yet"
            # raise ValueError("There is no courses created")
        # get_by_teacher_name = "SELECT name, programme FROM courses WHERE teacher=%s"
        cursor.execute("SELECT name, programme FROM courses WHERE teacher=?", (self.name, ))
        courses = cursor.fetchall()
        cursor.close()
        return courses

    def __str__(self):
        db_connection = sqlite3.connect('coursefactory.db')
        cursor = db_connection.cursor()
        cursor.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='teachers' ")
        if cursor.fetchone()[0] == 0:
            # raise ValueError("There is no teachers added yet")
            return "There is no teachers added yet"
        cursor.execute("SELECT name FROM teachers WHERE name=?",
                       (self.name, ))
        teacher = cursor.fetchone()
        cursor.close()
        return f"Teacher - {teacher[0]}\n"


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def add_teacher(name):
        pass

    @staticmethod
    @abstractmethod
    def create_local_course(name, teacher, programme, lab):
        pass

    @staticmethod
    @abstractmethod
    def create_offsite_course(name, teacher, programme, place):
        pass


class CourseFactory(ICourseFactory):
    @staticmethod
    def add_teacher(name):
        return Teacher(name)

    @staticmethod
    def create_local_course(name, teacher, programme, lab):
        return LocalCourse(name, teacher, programme, lab)

    @staticmethod
    def create_offsite_course(name, teacher, programme, place):
        return OffsiteCourse(name, teacher, programme, place)


def main():
    try:
        stepik = CourseFactory()
        teacher = stepik.add_teacher("Datsiuk Oksana Antonivna")
        local = stepik.create_local_course("Databases", teacher, ["MySQL", "SQLite", "MongoDB", "PostgreSQL"], "Lab 5-15")
        offsite = stepik.create_offsite_course("NoSQL", teacher, ["NoSQL foundations", "Intermediate NoSQL", "Advanced NoSQL"], "Kyiv")
        print(teacher)
        print(local)
        print(offsite)

    except TypeError as e:
        print(e)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()