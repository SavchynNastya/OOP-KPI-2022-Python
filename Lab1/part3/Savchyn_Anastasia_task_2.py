class Time:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Hour should be an integer")
        elif not 0 <= val <= 23:
            raise ValueError("Hour should be 0-23")
        self.__hour = val

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Minutes should be an integer")
        elif not 0 <= val <= 59:
            raise ValueError("Minutes should be 0-59")
        self.__minutes = val

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, val):
        if not val or not isinstance(val, int):
            raise TypeError("Seconds should be an integer")
        elif not 0 <= val <= 59:
            raise ValueError("Seconds should be 0-59")
        self.__seconds = val

    def __convert_to_american(self):
        if self.hour > 12:
            hour = self.hour - 12
            hour = str(hour) + ' p'
        if self.hour <= 12:
            hour = str(self.hour) + ' a'
        return hour

    def get_full(self):
        return f"{self.hour} hours {self.minutes} minutes {self.seconds} seconds"

    def get_american(self):
        hour = self.__convert_to_american()
        return f"{hour}.m  {self.minutes} minutes {self.seconds} seconds"


def main():
    try:
        t1 = Time(8, 5, 6)
        t2 = Time(15, 2, 9)

        print(t1.get_full())
        print(t1.get_american())

        print(t2.get_full())
        print(t2.get_american())

    except TypeError as e:
        print(str(e))
    except ValueError as e:
        print(str(e))


if __name__ == "__main__":
    main()
