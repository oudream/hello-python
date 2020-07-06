import functools
import sys

"""
---------------------- function decorator ----------------
"""


# 构建不带参数的装饰器
def logging(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print(("%s called" % func.__name__))
        result = func(*args, **kwargs)
        print(("%s end" % func.__name__))
        return result

    return decorator


# 使用装饰器
@logging
def test01(a, b):
    print(("in function test01, a=%s, b=%s" % (a, b)))
    return 1


# 使用装饰器
@logging
def test02(a, b, c=1):
    print(("in function test02, a=%s, b=%s, c=%s" % (a, b, c)))
    return 1


"""
---------------------- class decorator ----------------
"""


def addID(original_class):
    orig_init = original_class.__init__

    # Make copy of original __init__, so we can call it without recursion

    def __init__(self, id, *args, **kws):
        self._name = type(self).__name__
        self._id = id
        self._id1 = '1111'
        self._id2 = '22222'
        self._id3 = '33333'
        orig_init(self, *args, **kws)  # Call the original __init__

    original_class.__init__ = __init__  # Set the class' __init__ to the new one
    return original_class


@addID
class Foo:
    @classmethod
    def hello(cls):
        print('hello:')
        print(sys.getsizeof(cls))
        print(cls.__basicsize__)
        print(cls.__itemsize__)

    def show(self):
        print('show:')
        print(sys.getsizeof(self))
        print(self._id)
        print(self._id1)
        print(self._id2)
        print(self._id3)
        print(sys.getsizeof(self))
        print(self._name)


if __name__ == '__main__':
    """
    ---------------------- function decorator ----------------
    """
    # test01('aa', 'bb')
    # test02('aa', 'bb')
    foo = Foo('hello-id1')
    foo.show()
    #
    Foo.hello()
    print('end -------------')