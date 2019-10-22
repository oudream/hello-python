import test_class_visible_1 as human


class Person(human.Human):
    def say(self):
        print(('i am ', self.__class__.__name__))
        # print(self.__name) #error visible
        print((self._name))
        print((self.name))


h = human.Human()
print((h.name))
print((h._name))
# print(h.__name) #error visible

p = Person()
p.say()


class Ca:
    # _a = None
    # __a = None
    def __init__(self):
        self._a = "a"
        self.__a = "b"

    def Get_a(self):
        return self.__a


class Cb(Ca):
    def CName(self):
        self._b = "_b"
        return self._a


def Say():
    print("Big Say")


def say():
    print("small say")


# Say()

a = Cb()
s = a.CName()
ss = a._b
print(ss)
print(s)
