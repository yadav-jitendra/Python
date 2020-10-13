class Coordinate(object):
    x = 100
    y = 200

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return dist

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    # def __len__(self):
    #     origin = Coordinate(0, 0)
    #     other = Coordinate(self.x, self.y)
    #     length = Coordinate.distance(origin, other)
    #     return float(length)


k = Coordinate(3, 4)
g = k
h = Coordinate(2, 7)
origin = Coordinate(0, 0)

print(Coordinate.distance(k, h))
print(Coordinate.distance(origin, h))

print(k.distance(h))
print(k)
print(h)
print(k + h)
print(Coordinate.x)
print(k.x)
print('istance of coord: ', isinstance(k, Coordinate))
print('is g a k?: ', g is k)
print('instance of object: ', isinstance(k, object))
print(type(k))
