# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/10
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
import uiautomator2 as u2
import time

d = u2.connect('127.0.0.1:7555')  # 连接mumu虚拟机
d.app_start("com.kuaishou.nebula")  # 打开快手极速版

