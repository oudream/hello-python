# import sys
#
# sys.path.append('.')
import codecs

from hello.module1 import class2
from hello.module1 import singleton


def run():
    class2.show_age2()
    print('hello1-run: ')
    s = singleton.Singleton.getInstance()
    s.show()
    # codecs.encode()


print('__name__'+__name__)


if __name__ == '__main__':
    run()
else:
    run()
