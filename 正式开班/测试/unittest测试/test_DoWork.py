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
import sys
import unittest
from typing import List

import pandas as pd

from DoWork import DoWork
from DoWork01 import DoWork1
from ddt import data, file_data, ddt, unpack

from HTMLTestRunner import HTMLTestRunner


def get_csvdata(path):
    df = pd.read_csv(path)
    data = list(df['testcase'].astype('str'))
    data1 = []
    for i in data:
        if len(i) == 1 :
            data1.append(list(i))
        else:
            j = []
            j.append(i)
            data1.append(j)
    return data1


@ddt
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
    # @unittest.skipIf(sys.platform=='win132','啦啦啦啦！')
    # @unittest.skipIf(sys.version=='3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)]','是3.9版本的！')
    @data('1','2')
    # @unpack
    def test_01(self, a):
        print(a)

    # @file_data('test_data.yaml')
    # def test_a(self, *args):
    #     print(args[0])
    a = get_csvdata('test_data.csv')
    @data(*a)
    @unpack
    def test_02(self,c):
        print(c)

    # def test_a_run(self):
    #     print('输入4, 6, 9')
    #     print(DoWork(4, 6, 9))
    #     print('输入10,6')
    #     print(DoWork1(10, 6))
    #
    # def test_b_run(self):
    #     print('输入4, 4, 9')
    #     print(DoWork(4, 4, 9))
    #     print('输入7,4')
    #     print(DoWork1(7, 4))
    #
    # def test_c_run(self):
    #     print('输入4, 6, 11')
    #     print(DoWork(4, 6, 11))
    #     print('输入17,11')
    #     print(DoWork1(17, 11))
    #
    # def test_d_run(self):
    #     print('输入5, 6, 9')
    #     print(DoWork(5, 6, 9))
    #     print('输入1,1')
    #     print(DoWork1(1, 1))
    #
    # def test_e_run(self):
    #     print('输入5, 4, 9')
    #     print(DoWork(5, 4, 9))
    #     print('输入-1,-1')
    #     print(DoWork1(-1, -1))
    #
    # def test_f_run(self):
    #     print('输入5, 6, 11')
    #     print(DoWork(5, 6, 11))
    #
    # def test_g_run(self):
    #     print('输入3, 4, 11')
    #     print(DoWork(3, 4, 11))
    #
    # def test_h_run(self):
    #     print('输入3, 4, 9')
    #     print(DoWork(3, 4, 9))
    #
    # def test_i_run(self):
    #     print('输入3, 6, 9')
    #     print(DoWork(3, 6, 9))
    #
    # def test_k_run(self):
    #     print('输入3, 6, 9')
    #     print(DoWork(3, 6, 9))

#
# if __name__ == '__main__':
# suite=unittest.TestSuite()
# suite.addTest(unittest.TestLoader().loadTestsFromName("MyTest.test_01"))
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(MyTest))
# with open('result.html','wb') as f:
#     # runner=unittest.TextTestRunner(stream=f,verbosity=2)
#     runner=HTMLTestRunner(stream=f, title="测试报告", description="用例执行情况")
#     runner.run(suite)
