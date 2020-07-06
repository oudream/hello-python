import datetime
import time
import unittest

import pytest


class TestGoods(object):

    @pytest.mark.goods
    @pytest.mark.run(order=2)
    def test_goods_social(self, browser):
        print('-------------- i am goods --------------------%s' % browser)


if __name__ == '__main__':
    pytest.main(['-s', 'goods_test.py'])
