class A(object):
    def __init__(self):
        self.c = 'o'

    def set(self, a, b):
        print(a, b)
        print(self.c)


def hello1():
    a = A()
    c = getattr(a, 'set')
    c(a='1', b='2')
    hello2(c)

def hello2(m):
    m(3, 4)


if __name__ == '__main__':
    hello1()
