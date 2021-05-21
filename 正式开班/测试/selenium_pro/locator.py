# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/21
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
from selenium.webdriver.common.by import By


class Locator:
    # 定位元素变量名=元组（定位方式,'定位具体值'）
    search_text = (By.ID, 'sb_form_q')
    search_btn = (By.ID, 'sb_form_go')
