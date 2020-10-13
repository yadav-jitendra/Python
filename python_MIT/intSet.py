class intSet(object):
    def __init__(self):
        self.myList = []

    def insert(self, element):
        if element not in self.myList:
            self.myList.append(element)
            print(element, 'inserted')
        else:
            print(element, 'already in the Set. Not inserted')

    def member(self, element):
        return element in self.myList

    def remove(self, element):
        try:
            return self.myList.remove(element)
            print(elemant, 'removed')
        except:
            print(str(element), 'not in the Set so not removed')

    def __str__(self):
        self.myList.sort()  # so that element in the set will be represented in ascending oder
        printElement = ''
        for element in self.myList:
            printElement = printElement + str(element) + ','
        return '{' + printElement[:-1] + '}'


s = intSet()
print(s)
s.remove(3)
s.insert(3)
s.insert(2)
s.insert(3)
print(s)
s.remove(7)
print(s.member(3))
print(s.member(10))
