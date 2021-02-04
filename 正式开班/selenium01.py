# -*- coding: UTF-8 -*-
import selenium

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/2/4 15:58
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
from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
element = wd.find_element_by_id('kw')
print(element.text)
element.send_keys('梁志超是谁？')
# wd.quit()