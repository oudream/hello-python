import os
import sys


def hello1():
    for i in range(0, 5):
        print(str(i) + '\n')


if __name__ == '__main__':
    hello1()
    print(sys.argv)
    print(os.getcwd())
