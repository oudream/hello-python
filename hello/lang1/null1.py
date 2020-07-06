def hello1():
    s1 = ''
    if s1:
        print('y')
    else:
        # n
        print('n')


def hello2():
    s1 = None
    if s1 is None:
        # y
        print('y')
    else:
        print('n')


def hello3():
    s1 = 0
    if s1:
        print('y')
    else:
        # n
        print('n')


def hello4():
    s1 = -1
    if s1:
        # y
        print('y')
    else:
        print('n')


def hello5():
    def fn1():
        return

    s1 = fn1()
    if not s1:
        # y
        print('y')
    else:
        print('n')


def hello6():
    """
    'NoneType' object is not iterable
    Returns:

    """
    s1 = None
    try:
        for i in s1:
            print('hello6')
    except Exception as e:
        # print(e)
        print(e)


def hello7():
    """
    argument of type 'NoneType' is not iterable
    Returns:

    """
    s1 = None
    try:
        if 1 in s1:
            print('hello7 in')
        else:
            print('hello7 not in')
    except Exception as e:
        # print(e)
        print(e)


def hello8():
    """
    '>' not supported between instances of 'int' and 'NoneType'
    Returns:

    """
    s1 = None
    try:
        if 1 > s1:
            print('hello8 >')
        else:
            print('hello8 <')
    except Exception as e:
        # print(e)
        print(e)


def hello9():
    arr = ['aa', 'bb']
    arr.clear()
    if arr:
        print("hello9 y")
    else:
        print("hello9 n")


def hello10(ele):
    def show():
        print('-----------show 9')
    return show() or True if ele else False


if __name__ == '__main__':
    hello1()
    hello2()
    hello3()
    hello4()
    hello5()
    hello6()
    hello7()
    hello8()
    hello9()
    print('----------------10 -:' + str(hello10(1)))
