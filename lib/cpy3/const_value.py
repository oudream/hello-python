import os
import sys


class ConstValue(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        def __init__(self):
            pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            # if name in self.__dict__:
            raise (self.ConstError, 'Not allowed change const.{value}'.format(value=name))
        if not name.isupper():
            raise (self.ConstCaseError, "Const's name is not all uppercase")
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise (self.ConstError, "Can't unbind const const instance attribute (%s)" % name)
        raise (AttributeError, "const instance has no attribute '%s'" % name)


sys.modules[__name__] = ConstValue()
