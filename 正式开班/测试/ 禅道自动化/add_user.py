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


class Add_user(Basepage):

    def main_add_user(self, user_name_data, login_password):
        search_page = Basepage(self.driver)
        search_page.click_organization(Locator.organization_submit)
        search_page.click_add_user_submit(Locator.add_user_submit)
        search_page.click_department(Locator.department_submit)
        search_page.click_department_02(Locator.department)
        search_page.input_password_one(Locator.password_one, login_password)
        search_page.input_password_two(Locator.password_two, login_password)
        search_page.input_realname(Locator.realname, 'chenluobo')
        search_page.verify_Password(Locator.verify_Password, login_password)
        search_page.input_user_name(Locator.user_name, user_name_data)
        search_page.add_submit(Locator.add_submit)
