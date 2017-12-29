class A(object):
    def show(self):
        print("enter A")
        print("leave A")


class B(object):
    def show(self):
        print("enter B")
        print("leave B")


class C(object):
    # def __init__(self):
    # A.__init__(self)
    # B.__init__(self)

    def show(self):
        print("enter C")
        # super(A, self).show()
        print("leave C")


class D(C, B, A):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        A.__init__(self)

    def show(self):
        print("enter D")
        B.show(self)
        # super(B, self).show()
        # A.show(self)
        print("leave D")


class E(A, B):
    def show(self):
        print("enter E")
        B.show(self)
        C.show(self)
        print("leave E")


def hello():
    print('hello')


class A(object):
    def show(self):
        print('A')


c = D()
c.show()
c.hello = hello
c.hello()
# del c.show
# c.show()
