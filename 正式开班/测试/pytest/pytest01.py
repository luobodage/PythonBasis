# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/18
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
import random
import sys

import pytest


def add(x):
    return x + 2


class TestClass(object):
    # 测试是否相等
    def test_add(self):
        assert add(3) == 5

    # 测试包含
    def test_in(self):
        a = 'hello world'
        b = 'he'
        assert b in a

    @pytest.mark.skipif(sys.platform == 'win32', reason='你是windows不能运行！！！')
    def test_in01(self):
        assert 'luobo1' == 'luobo'

    def test_in02(self):
        assert 'luobo' * 20 == 'luobo' * 30

    @pytest.mark.webtest
    def test_web01(self):
        assert 'web' == 'web1'

    @pytest.mark.Androidtest
    @pytest.mark.last
    def test_app01(self):
        assert 'android' == 'Android'

    @pytest.mark.iostest
    def test_ios01(self):
        assert 'ios' == 'Android'

    def test_random01(self):
        result = random.randint(1, 10)
        pytest.assume(1 == 2)
        print('随机值为:', result)
        assert result == 9
    # # 测试不包含
    # def test_not_in(self):
    #     a = 'Hello'
    #     b = 'hi'
    #     assert b not in a


if __name__ == '__main__':
    # pytest.main(['-s', 'pytest01.py', '-m', 'Androidtest'])
    pytest.main(['-s', 'pytest01.py'])
