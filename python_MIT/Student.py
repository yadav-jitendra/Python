from python_MIT.MITPerson import MITPerson


class Student(MITPerson):
    pass


class UG(Student):
    def __init__(self, fullname, semNr):
        MITPerson.__init__(self, fullname)
        self.semNr = semNr

    def getSemNr(self):
        return self.semNr

    def speak(self, statement):
        MITPerson.speak(self, 'Dude' + statement)


class Grad(Student):
    pass


class Transferstudent(Student):
    pass


def isStudent(self):
    return isinstance(self, Student)


u1 = UG('jitendra yadav', 6)
g1 = Grad('ram kumar')
t1 = Transferstudent('sham prasad')

print(isStudent(t1))
print(t1.getAge())
