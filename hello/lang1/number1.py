import math
import random


def hello1():
    f1 = 1.51
    f2 = 1.49
    print(math.ceil(f1))
    print(math.ceil(f2))
    print(math.floor(f1))
    print(math.floor(f2))
    print(round(2.304, 2))
    print(round(2.306, 2))
    print(round(2.305, 2))
    print(round(2.675, 1))
    print(round(2.645, 1))


def hello2():
    """
    可能会重复
    Returns:

    """
    for i in range(5):
        L1 = random.randint(1, 10)
        print(L1, end=' ')


def hello3():
    """
    可能会重复
    Returns:

    """
    L1 = random.sample(range(1, 10), 5)
    print(L1)


if __name__ == '__main__':
    # hello1()
    hello2()
    hello3()
