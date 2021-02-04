# -*- coding: UTF-8 -*-

import requests

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/4 8:48
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
data = {
    'mysize': 100
}

a = requests.post(url='http://jiekou.laiyue.work',data=data).json()
print(a)
