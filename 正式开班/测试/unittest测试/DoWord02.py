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
import pyforest


def DoWord(iRecordNum, iType):
    x, y = 0, 0
    while iRecordNum < 0:
        if iType == 0:
            x = y + 2
        else:
            if iType == 1:
                x = y + 10
            else:
                x = y + 20
        iRecordNum -= 1

