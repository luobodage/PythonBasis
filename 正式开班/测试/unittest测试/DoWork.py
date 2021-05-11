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
import math


k, j = 0, 0


def DoWork(x, y, z):
    if x > 3 and z < 10:
        k = x * y - 1
        j = math.sqrt(k)

    if x == 4 or y > 5:
        j = x * y + 10
        j = j % 3
        return j


