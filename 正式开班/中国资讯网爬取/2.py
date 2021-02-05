# -*- coding: UTF-8 -*-

import requests

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/5 14:37
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
url = 'http://152.136.152.189:39999/'
data = {
    'mysize': 6
}
proxies = {
    'http': '60.167.134.11:8888'
}
content = requests.post(url=url, data=data, proxies=proxies, timeout=10).json()
print(content)
