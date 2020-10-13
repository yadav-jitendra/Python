import datetime


class person(object):
    def __init__(self, fullname):
        """Creates a person giving Full name"""
        self.pname = fullname
        self.birthday = None
        first_and_lastname = fullname.split()  # split first and last name and put them in a list
        self.lastname = first_and_lastname[-1]  # last name is the last element in the list
        self.firstname = fullname.split()[0:-1]

    def get_lastname(self):
        """Returns the last name of self"""
        return self.lastname

    def setBirthday(self, day, month, year):
        """sets birthday"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """gets current age """
        if self.birthday is None:
            raise ValueError('No bithdate provided')
        noOfdays = (datetime.date.today() - self.birthday).days
        return int(noOfdays / 365)

    def __str__(self):
        """Returns the fullname of the person"""
        return self.pname


ram = person('Ram kumar Yadav')
print(ram)
print('lastname :', person.get_lastname(ram))
ram.setBirthday(5, 10, 1990)
print(ram.getAge())
