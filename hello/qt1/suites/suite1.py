import unittest, pytest

from cases.login_test import TestLogin

from cases.goods_test import TestGoods


def suite():  # 创建测试添加测试套件函数
    suite = unittest.TestSuite()  # 建立测试套件
    suite.addTests([TestLogin('test_login'), TestGoods('test_goods_social')])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
