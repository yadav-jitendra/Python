class Fraction(object):
    def __init__(self, numerator, denomerator):
        self.numer = numerator
        self.denom = denomerator

    def __str__(self):
        return str(self.numer) + '/' + str(self.denom)

    def getNumer(self):
        return self.numer

    def getDenom(self):
        return self.denom

    def __add__(self, other):
        newNumer = self.getNumer() * other.getDenom() + other.getNumer() * self.getDenom()
        newDenom = self.getDenom() * other.getDenom()
        return Fraction(newNumer, newDenom)

    def convert(self):
        return self.numer / self.denom


k = Fraction(-25, 5)
h = Fraction(3, 4)
print(k)
print(k.denom)
print(k.getDenom())
print(k + h)
print(k.convert())
