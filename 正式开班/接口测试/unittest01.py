# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/04/16
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

import unittest


# 新建一个测试类 必须以Test开头 从unittest框架中继承测试用例
class TestIfDemo(unittest.TestCase):
    def setUp(self) -> None:
        print('这个方法是框架提供的，我们重写一下，这个方法是在测试方法执行前执行的！')

    def tearDown(self) -> None:
        print('这个方法是框架提供的，我们重写一下，这个方法是在测试方法执行后执行的！')

    def test_list_user_get(self):
        print('1234 2234')
        assert 1 == 2
        # 把我们写的接口代码复制过来

    def test_list_user_post(self):
        print('3234 4234')
        assert 'hello' in 'hello luobo'
        # 把我们写的接口代码复制过来

    def test_number(self):
        assert {'name': 'luobo'} == {'name': 'yupian'}

    def test_number_list(self):
        assert [1, 2, 3, 5] == [1, 2, 3, 4]


if __name__ == '__main__':
    unittest.main()

