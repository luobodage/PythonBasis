# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/19
# software: PyCharm
#         =    =     =
#          =   =   =
#           =  =  =
#         ===========
#         =   萝    =
#         =   卜    =
#         =   神    =
#         =   保    =
#         =   佑    =
#         =   永    =
#         =   无    =
#         =   bug  =
#          =      =
#           =    =
#              =
import pytest


@pytest.fixture(scope='module', autouse=True)
def open_close_browser():
    print('open browser!')
    yield
    print('close browser!')


def test_login():
    print('登录')


def test_seach():
    print('查看')
