
import sys

# --- --- --- --- ---
# list loop --
# --- --- --- --- ---

def testListLoop1():
    a = ["a", "b", "c", "d"]
    # simple iterate
    for i in a:
        print(i)

testListLoop1()


def testListLoop2():
    a = ["a", "b", "c", "d"]
    # index & value
    for i in range(len(a)):
        print(i, a[i])

testListLoop2()


def testListLoop3():
    a = ["a", "b", "c", "d"]
    # iterate with index
    for i, el in enumerate(a):
        print(i, el)

testListLoop3()


# --- --- --- --- ---
# list create --
# --- --- --- --- ---
def testList11():
    a = [None] * 10
    a = list(range(10))
    a = [None for i in range(10)]
    print(a)

testList11()


def testList12():
    import re
    import random
    subs = list(range(1, 100))
    for i in range(0, len(subs), 1):
        subs[i] = '{0}{1}{2}'.format(i, '-a', i)
    print(subs)
    # for sub in subs:
    #     print(sub)
    random.shuffle(subs)
    print(subs)
    print(re.sub(r'\(.*\)', '( )', 'x * y = ( 55 )'))

testList12()
