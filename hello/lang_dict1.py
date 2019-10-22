# --- --- --- --- ---
# dict loop --
# --- --- --- --- ---

def testLoopDict1():
    # construct 1
    l = [(x, x) for x in range(10000)]
    d = dict(l)

    from time import clock

    t0 = clock()
    for i in d:
        t = i + d[i]
    t1 = clock()

    for k, v in list(d.items()):
        t = k + v
    t2 = clock()

    for k, v in list(d.items()):
        t = k + v
    t3 = clock()

    for k, v in zip(list(d.keys()), list(d.values())):
        t = k + v
    t4 = clock()

    print((t1 - t0, t2 - t1, t3 - t2, t4 - t3))

    enumm = {0: 1, 1: 2, 2: 3, 4: 4, 5: 5, 6: 6, 7: 7}

    for i, j in enumerate(enumm):
        print((i, j))


# testLoopDict1()


'''
A = { 
    'a': {
        'A': {
            '1': {}, 
            '2': {}, 
        },  
        'B': {
            '1': {}, 
            '2': {}, 
        },  
    },  
    'b': {
        'A': {
            '1': {}, 
            '2': {}, 
        },  
        'B': {
            '1': {}, 
            '2': {}, 
        },  
    },  
}
'''


def testMultidict():
    from copy import copy

    def multidict(*args):
        if len(args) == 1:
            return copy(args[0])
        out = {}
        for x in args[0]:
            out[x] = multidict(*args[1:])
        return out

    print((multidict(['a', 'b'], ['A', 'B'], ['1', '2'], {})))


def testLoopDict2():
    _locals = locals()
    print(_locals)
    for i in _locals:
        print(i)
    d = {'x': 1, 'y': 2, 'z': 3}
    for key in d:
        print(key)


# testLoopDict2()

d = dict(locals())
for k, v in list(d.items()):
    print((k, v))
