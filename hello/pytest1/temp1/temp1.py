import sys

import pytest

class TestTemp1:

    def test_temp1a(self):
        from config.config import Config
        print(Config.cpu())

    def test_temp1c(self):
        print('------------------------- test_temp1c : %s' % sys.path)

    def temp1b(self):
        from config.config import Config
        print(Config.cpu())


