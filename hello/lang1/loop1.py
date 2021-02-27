import os
import sys


def hello1():
    for i in range(0, 5):
        print(str(i) + '\n')


def hello2():
    """
    https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    Returns:

    """
    a = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    # >> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    # sample to
    # combs = []
    # for x in [1, 2, 3]:
    #     ...
    #     for y in [3, 1, 4]:
    #         ...
    #     if x != y:
    #         ...
    #     combs.append((x, y))
    print(a)


if __name__ == '__main__':
    # hello1()
    # print(sys.argv)
    # print(os.getcwd())
    hello2()
