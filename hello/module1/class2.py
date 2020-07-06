from hello.module1 import class1
from hello.module1 import singleton


def show_age2():
    print(class1.ages)
    ages = class1.ages.items()
    for x, y in ages:
        print(x, y)
    # for x, y in class1.PROXY_LIST:
    #     print(x, y)
    # for x in class1.ages:
    #     print(x)
    class1.show_age1()
    print('show_age1: ')
    s = singleton.Singleton.getInstance()
    s.show()


print('__name__'+__name__)
