import os


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError

        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError
        raise AttributeError


# import sys
# sys.modules[__name__] = _const()


class ConstValue(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        def __init__(self):
            pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            # if name in self.__dict__:
            raise self.ConstError
        if not name.isupper():
            raise self.ConstCaseError
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError
        raise AttributeError


const = ConstValue()
const.GOOD = 1
const.BAD = 2


def testConst1():
    const.GOOD = 1
    del const.BAD
    pass


testConst1()
