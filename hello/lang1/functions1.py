import functools
import math
import time
from datetime import datetime

"""
------------------------ filter --------------
"""


# 构建不带参数的装饰器
def logging(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        # now = math.floor(datetime.now().timestamp() * 1000)
        count = time.perf_counter_ns()
        print(("---------------- %s called" % func.__name__))
        result = func(*args, **kwargs)
        # diff = math.floor(datetime.now().timestamp() * 1000) - now
        diff = time.perf_counter_ns() - count
        print("---------------- %s end. cost time : %d" % (func.__name__, diff))
        return result

    return decorator


@logging
def hello1():
    newlist = filter(lambda n: n % 3 == 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # print(newlist)
    # Python3.6结果：<filter object at 0x00000184ED881358>
    # Python2.x结果：[1, 3, 5, 7, 9]
    # Python3.6返回的是迭代器对象，可以转换成list
    print(list(newlist))
    # time.sleep(1)


@logging
def hello2():
    def is_odd(n):
        return n % 2 == 1

    newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(list(newlist))


@logging
def hello3():
    newlist = list(x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 == 1)
    print(newlist)


if __name__ == '__main__':
    hello1()
    hello2()
    hello3()
