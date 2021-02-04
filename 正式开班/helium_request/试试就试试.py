# -*- coding: UTF-8 -*-

from helium import *
import requests
import time

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/4 16:25
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
# driver = get_driver()
driver = start_chrome('https://phat.jd.com/10-507.html')  # 访问jd页面
scroll_down(num_pixels=1000000)  # 下拉到最后
time.sleep(10)  # 睡眠10秒 等待页面刷新
element = driver.execute_script("return document.documentElement.outerHTML")  # 获取html代码
with open('jd.html', 'w', encoding='utf8') as f:
    f.write(element)
