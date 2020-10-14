from inheritance.Person import Person


class MITPerson(Person):
    nextID = 0  # next ID num to assign

    def __init__(self, fullname):
        Person.__init__(self, fullname)
        self.idNum = MITPerson.nextID
        MITPerson.nextID += 1

    def getID(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def speak(self, statement):
        return self.get_lastname() + ' says ' + statement

# # trial
# m3 = MITPerson('Mark Zuckerberg')
# # Person.setBirthday(m3, 5, 1, 84)
# m2 = MITPerson('Drew Houston')
# # Person.setBirthday(m2, 3, 4, 83)
# m1 = MITPerson('Bill Gates')
# # Person.setBirthday(m1, 10, 2, 55)
# p1 = Person('jitendra yadav')
#
# MITPersonList = [m1, m2, m3]
#
# for e in MITPersonList:
#     print(f'{e} - ID: {e.idNum}')
#
# print('###################')
#
# MITPersonList.sort()
# for e in MITPersonList:
#     print(f'{e} - ID: {e.idNum}')
#
#
# print('###########')
# print(m1.speak('hello there!'))

# print(isinstance(p1, MITPerson))
# print(isinstance(m1, Person))
