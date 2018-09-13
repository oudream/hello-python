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

def yes():pass

a=yes


def yes():pass
print('---0')
print(show)
print('---2')
print(type(show))
print('---1')
print(show.__name__)
print('---11')
print(show.__qualname__)
print('---12')
print(show.__module__)
print('---13')
print(show.__code__)
code = show.__code__
print(code.co_argcount)
print(code.co_varnames)
print(inspect.getsource(show))
print('---14')
print(show.__annotations__)
print('---')



class ClassA:
    pass
