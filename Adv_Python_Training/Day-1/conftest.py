import pytest


@pytest.fixture(scope='module')
def amounts():
    ams = [100, -200, 300, -400, 400]
    return ams