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
from locator import Locator
from base_page import Basepage


class Login_page(Basepage):

    def main_login(self, login_username,login_password):
        search_page = Basepage(self.driver)
        search_page.input_username(Locator.login_user, login_username)
        search_page.input_password(Locator.login_password, login_password)
        search_page.click_login_button(Locator.login_submit)
