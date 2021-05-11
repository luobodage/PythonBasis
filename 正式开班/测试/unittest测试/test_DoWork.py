# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/11
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
from DoWork import DoWork


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('测试结束')
        print('----------------')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('----------------')
        print('测试开始')

    # @classmethod
    # def tearDownClass(self):
    #     # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
    #     print('4444444')
    #
    # @classmethod
    # def setUpClass(self):
    #     # 必须使用@classmethod 装饰器,所有test运行前运行一次
    #     print('33333')

    def test_a_run(self):
        print('输入4, 6, 9')
        print(DoWork(4, 6, 9))

    def test_b_run(self):
        print('输入4, 4, 9')
        print(DoWork(4, 4, 9))

    def test_c_run(self):
        print('输入4, 6, 11')
        print(DoWork(4, 6, 11))

    def test_d_run(self):
        print('输入5, 6, 9')
        print(DoWork(5, 6, 9))

    def test_e_run(self):
        print('输入5, 4, 9')
        print(DoWork(5, 4, 9))

    def test_f_run(self):
        print('输入5, 6, 11')
        print(DoWork(5, 6, 11))

    def test_g_run(self):
        print('输入3, 4, 11')
        print(DoWork(3, 4, 11))

    def test_h_run(self):
        print('输入3, 4, 9')
        print(DoWork(3, 4, 9))

    def test_i_run(self):
        print('输入3, 6, 9')
        print(DoWork(3, 6, 9))

    def test_k_run(self):
        print('输入3, 6, 9')
        print(DoWork(3, 6, 9))


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
