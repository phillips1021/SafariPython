
class Date:
    # self is equivalent to "this" in C++ derived languages
    def __init__(self, day, month, year):
        self.__day = day ## no private, we're all consenting adults here.
        self.__month = month  ## self prefix is mandatory!!!
        self.__year = year
        print("initializing a date")

    def __repr__(self):  ## "representation" of object--how you would be seen in source literal
        return f"Date(self.day, self.month, self.year)"
        # return self.__str__()

    # "overriding" instance methods, normal instance methods are essentially the same
    def __str__(self):
        return f"I'm a date, day is {self.__day}"

    @staticmethod
    def is_leap_year(year):
        # % is mod, not remainder
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    # take care & and | exist, but are intended to be used as bitwise operators.

class Oddball:
    def __init__(self):
        print("initializing oddball")

class Holiday(Date, Oddball):
    def __init__(self, d, m, y, name):
        self.name = name
        # shorthand for "my first superclass" is simply super()
        # super().__init__(d, m, y)
        # "full form" is "class to left", self
        super(Holiday, self).__init__(d, m, y)
        # for the specific superclass "to the right of Date", i.e. Oddball
        super(Date, self).__init__()
        print("Initializing a Holiday")

d = Date(11, 4, 2022)
d.weekday = "Monday"
print(d)
print(type(d))
# "name mangling" attempts to "hide" what would otherwise be private
print(f"date has: day = {d._Date__day} and weekday = {d.weekday}")

days = [d, Date(1, 1, 2000)]
print(days)

print(f"2000 is a leap year? {Date.is_leap_year(2000)}")

h = Holiday(1, 1, 2023, "New Year's Day")
print(type(h))
print(h)
