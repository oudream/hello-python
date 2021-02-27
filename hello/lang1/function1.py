import inspect


def show(fn, a, b):
    '''
    sss asd
    :param fn:
    :param a:
    :param b:
    :return: null
    '''
    fn(a, b)
    pass


def yes(): pass


a = yes


def yes(): pass


def hello1():
    print('---0')
    print(show)
    print('---2')
    print((type(show)))
    print('---1')
    print((show.__name__))
    print('---11')
    print((show.__qualname__))
    print('---12')
    print((show.__module__))
    print('---13')
    print((show.__code__))
    code = show.__code__
    print((code.co_argcount))
    print((code.co_varnames))
    print((inspect.getsource(show)))
    print('---14')
    print((show.__annotations__))
    print('---')


def hello2(a):
    _name = 'xxxxxxxx'

    def _hello2():
        print(_name)
        print(a)

    _hello2()


class ClassA:
    def hello2(self, a: str = 'eeeeeeee'):
        """

        Args:
            a:

        Returns:

        """
        _name = 'xxxxxxxx'

        def _hello2():
            print(_name)
            if a is str:
                print(a + '----->')
            print(a)

        _hello2()


def hello3():
    class C:
        def show(self):
            """"""
            print('dddddddddd')
            return 'ccccccccccc'

    i = 'iiiiiiiiiii'
    # hello = lambda : print( C().show() )
    hello = lambda C: exec('print( C().show() )')
    # hello = lambda : exec(
    # """a = 'aaaaaaaaaaaaaaaa';b = 'bbbbbbbbbb';print( a + b + i )""")

    hello(C)


def hello4(*arg, **kwargs):
    a1, a2, a3 = arg
    print(type(a1))
    print(type(a2))
    print(type(a3))
    print(a1)
    print(a2)
    print(a3)
    print(type(arg))
    print(arg)
    print(len(arg))
    print(type(kwargs))
    print(kwargs)
    print(len(kwargs))


def hello5(a1, *args):
    print(type(a1))
    print(a1)
    print(args)


if __name__ == '__main__':
    # hello1()
    # hello2('bbbbbbbbbbbb')
    # ClassA().hello2()
    p = 1, 2, 'abc'
    # hello4(*p, k1=7, k2='a')
    hello5(*p)
