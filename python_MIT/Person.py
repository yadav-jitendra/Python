import datetime


class Person(object):
    def __init__(self, fullname):
        """Creates a person giving Full name"""
        self.pname = fullname
        self.birthday = None
        first_and_lastname = fullname.split()  # split first and last name and put them in a list
        self.lastname = first_and_lastname[-1]  # last name is the last element in the list

    def get_lastname(self):
        """Returns the last name of self"""
        return self.lastname

    def setBirthday(self, day, month, year):
        """sets birthday"""
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        """gets current age """
        if self.birthday is None:
            raise ValueError('No birthdate provided')
        noOfdays = (datetime.date.today() - self.birthday).days
        return int(noOfdays / 365)

    def __str__(self):
        """Returns the fullname of the person"""
        return self.pname

    def __lt__(self, other):  # sort method will call this method internally
        """returns true if self lastname is lexicographically less than other lastname
            if both of them have same last name : compare with fullname
        """
        if self.lastname == other.lastname:
            return self.pname < other.pname
        return self.lastname < other.lastname

#
# # trial
# p1 = Person('Mark Zuckerberg')
# p1.setBirthday(5,1,1984)
# p2 = Person('Drew Houston')
# p2.setBirthday(3,4,1983)
# p3 = Person('Bill Gates')
# p3.setBirthday(10,2,1955)
# p4 = Person('Andrew Gates')
# p5 = Person('Steve Wozniak')
#
# l1 = [p1, p2, p3, p4,p5]
# for person in l1:
#     print(person)
#
# print('#############################')
#
# l1.sort()
# for person in l1:
#     print(person)
