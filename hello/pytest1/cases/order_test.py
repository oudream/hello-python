import time
import unittest

import pytest


class TestOrder(object):

    @pytest.mark.dependency(depends=["TestExample::test_a"])
    def test_c(self):
        # TestExample::test_a 没通过则不执行该条用例
        # 可以跨 Class 筛选
        print('-------------- i am TestOrder::test_c --------------------')

    @pytest.mark.dependency()
    def test_a(self):
        print('-------------- i am TestOrder::test_a --------------------')
        # assert False
        return True

    @pytest.mark.dependency()
    def test_b(self):
        # assert False
        print('-------------- i am TestOrder::test_b --------------------')

    @pytest.mark.dependency(depends=["TestExample::test_a", "TestExample::test_b"])
    def test_d(self):
        print('-------------- i am TestOrder::test_d --------------------')


if __name__ == '__main__':
    pytest.main(['-vs', 'order_test.py::TestOrder::test_c'])
