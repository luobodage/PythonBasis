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
from .locator import Locator
from .base_page import BasePage


class Search_page(BasePage):

    def home_search(self, test_data):
        BasePage.enter_text(*Locator.find_text, test_data)
        BasePage.click_all(*Locator.find_pushButton)
