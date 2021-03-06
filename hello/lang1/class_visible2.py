import lang_class_visible_1 as human


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


class Foo(object):
    _count = 0  # 不要直接操作这个变量，也尽量避免访问它

    @property
    def count(self):
        return Foo._count

    @count.setter
    def count(self, num):
        Foo._count = num


f1 = Foo()
f2 = Foo()
print(f1.count, f1._count, f2.count, f2._count)

f1.count = 1
print(f1.count, f1._count, f2.count, f2._count)


# Say()


class Foo(object):
    __count = 0  # 私有变量，无法在外部访问，Foo.__count会出错

    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def set_count(cls, num):
        cls.__count = num


f1 = Foo()
f2 = Foo()
Foo.set_count(1)
print(f1.get_count(), f2.get_count())

a = Cb()
s = a.CName()
ss = a._b
print(ss)
print(s)
