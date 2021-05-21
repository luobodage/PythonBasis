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
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

test_data = ['python', 'java', 'golang']


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @pytest.mark.parametrize('data', test_data, indirect=True)
    def input_text(self, loc, *data):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.clear()
        ele.send_keys(data)

    @pytest.mark.parametrize('data', test_data, indirect=True)
    def click_seacrh(self, loc):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.click()
