
import sys
import os

import pytest

# sys.path.append(os.getcwd())


if __name__ == '__main__':
    print(sys.path)
    pytest.main(['-vs', './cases/login_test.py::TestLogin::test_login_logout'])
    print(sys.path)
    # pytest.main(['-vs', './cases/order_test.py::TestOrder::test_c'])
