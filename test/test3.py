# b.py
from . import test1

def fn_test3_1():
    print((test1.gl_1, test1.gl_2))
    test1.gl_1 = 'test31'
    test1.gl_2 = 'test32'
