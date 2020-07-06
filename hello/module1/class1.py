
from hello.module1 import singleton


ages = {'a': 1, 'b': 2, 'c': 3}

high = {'a': 1.7, 'b': 2.1, 'c': 0.9}


def show_age1():
    # for x, y in class1.ages:
    #     print(x, y)
    # for x in class1.ages:
    #     print(x)
    s = singleton.Singleton.getInstance()
    s.name = 'name2'
    print('show_age2: ')
    s.show()


print('__name__'+__name__)
