

def getNumber(fn):
    print((fn(10)))


def lineConf():
    def line(x):
        return 2 * x + 1

    return line


# getNumber(lineConf())


def maker(m):
    k = 8

    def maker1(m1):
        m1 += 1

        def maker11(m11):
            m11 += 1
            return m11 + m1 + m + k

        return maker11

    return maker1


f = maker(2)(3)(4)
print(f)
