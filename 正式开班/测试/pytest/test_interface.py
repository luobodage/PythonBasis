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

# test_user_data = {
#     'username1': 'luobo',
#     'username2': 'yuyu',
#     'username3': 'ovo',
# }
test_user_data = ['干嘛~😊', '干嘛！😥', '干嘛！！🤬','你找死！！！👿']


@pytest.fixture
def login(request):
    print('打你一下~')
    return request.param


@pytest.mark.parametrize('login', test_user_data, indirect=True)
def test_run01(login):
    print(login)
