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
import time

from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    def __init__(self, drive):
        self.driver = drive

    def click_all(self, loc):
        """
        封装点击按钮 下面的点击操作直接调用这个函数就可以
        """
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.click()
        time.sleep(2)

    def say_keys_content(self, loc, search_data):
        """
        封装点击输入，下面调用直接调用这个方法
        """
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.click()
        ele.send_keys(search_data)
        time.sleep(1)

    def input_username(self, loc, search_data):
        """
        输入登录名
        """
        self.say_keys_content(loc, search_data)

    def input_password(self, loc, search_data):
        """
        输入登陆密码
        """
        self.say_keys_content(loc, search_data)

    def click_login_button(self, loc):
        """
        点击登录按钮进行登录
        """
        self.click_all(loc)

    def click_organization(self, loc):
        """
        点击组织按钮
        """
        self.click_all(loc)

    def click_add_user_submit(self, loc):
        """
        点击添加用户按钮进入添加用户界面
        """
        self.click_all(loc)

    def click_department(self, loc):
        """
        点击一下所属部门
        """
        self.click_all(loc)

    def input_user_name(self, loc, search_data):
        """
        选中所属部门
        """
        self.say_keys_content(loc, search_data)

    def click_department_02(self, loc):
        self.click_all(loc)

    def input_password_one(self, loc, search_data):
        self.say_keys_content(loc, search_data)

    def input_password_two(self, loc, search_data):
        self.say_keys_content(loc, search_data)

    def input_realname(self, loc, search_data):
        self.say_keys_content(loc, search_data)

    def verify_Password(self, loc, search_data):
        self.say_keys_content(loc, search_data)

    def add_submit(self, loc):
        """
        点击确认添加按钮
        """
        self.click_all(loc)
