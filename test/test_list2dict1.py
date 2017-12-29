
import sys

def testConstruct1():
    l = [(x, x) for x in range(10000)]
    d = dict(l)
    print(d)

def testConstruct2():
    print(dict(zip(*[iter(sys.argv[1:])]*2)))

def testConstruct3():
    l = [{'A': 123}, {'B': 234}, {'C': 345}]
    d = {k: v for dct in l for k, v in dct.items()}
    print(d)

def testConstruct4():
    string = [('limited', 1), ('all', 16), ('concept', 1), ('secondly', 1)]
    my_dict = dict(string)
    print(my_dict)

def testConstruct5():
    l = ["a", "b", "c", "d", "e"]
    print(dict(zip(l[::2], l[1::2])))

testConstruct1()
testConstruct2()
testConstruct3()
testConstruct4()
testConstruct5()

