class Animal(object):
    def __init__(self):
        self.legs = 2
        self.name = 'Dog'
        self.color = 'Spotted'
        self.smell = 'Alot'
        self.age = 10
        self.kids = 0
        self._height = 113

    @property
    def height(self):
        return self._height


def hello1():
    an = Animal()
    attrs = vars(an)
    _attrs = dir(an)
    # {'kids': 0, 'name': 'Dog', 'color': 'Spotted', 'age': 10, 'legs': 2, 'smell': 'Alot'}
    # now dump this in some way or another
    print(', '.join("%s: %s" % item for item in attrs.items()))
    for property, value in vars(an).iteritems():
        print(property, ": ", value)


if __name__ == '__main__':
    hello1()
