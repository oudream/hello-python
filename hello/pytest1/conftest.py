import logging

import pytest


@pytest.fixture(scope='session', autouse=True)
def browser():
    name = 'hello-browser1'

    yield name

    name = ''


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print('-------------- i am Hooks::pytest_runtest_setup --------------------')
