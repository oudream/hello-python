import os
import sys

print(sys.platform)

print(os.getcwd())

print('-------')


def test1():
    _locals = locals()
    for i in _locals:
        print(i)


test1()

_locals = locals()
for i in _locals:
    print(i)

print('-------')

print(globals())

print(__name__)
