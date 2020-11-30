from userh import *


def test_normal_user(amounts):

    u = NormalUser("Normal", 100)
    for am in amounts:
        u.transact(am)
    assert u.balance == 700


def test_Gold_user(amounts):

    u = GoldUser("Normal", 100)
    for am in amounts:
        u.transact(am)
    assert u.balance == 710


## pytest - v test_userh.py
## pytest --cov=userh --cov-report term-missing test_userh.py