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


@pytest.fixture
def login():
    print('登录！！')


@pytest.fixture
def data():
    print({'a': 'b'})
