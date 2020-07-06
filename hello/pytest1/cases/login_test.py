import sys
import time
import unittest

import pytest

from config.config import Config


class TestLogin(object):

    @pytest.mark.login
    @pytest.mark.run(order=1)
    def test_login(self, browser):
        print('-------------- i am login --------------------%s' % browser)

    @pytest.mark.hello
    @pytest.mark.run(order=3)
    def test_login_logout(self, browser):
        config = Config()
        print('-------------- i am login and logout --------------------%s - %s - %s' % (browser, Config.cpu(), sys.path))


if __name__ == '__main__':
    pytest.main(['-vs', 'login_test.py::TestLogin::test_login_logout'])
