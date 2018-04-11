
# --- --- --- --- ---
# dict loop --
# --- --- --- --- ---

def testLoopDict1():
    # construct 1
    l = [(x, x) for x in range(10000)]
    d = dict(l)

    from time import clock
    import time
    import calendar


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

testLoopDict1()

