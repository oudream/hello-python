
import sys

sys.path.append('..')

from . import glovar
from ..test import test1


class Calc:
    def add(self):
        glovar.x += 1
        test1.test11 += 2
