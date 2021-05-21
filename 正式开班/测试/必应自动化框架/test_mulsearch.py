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
from locator import Locator

test_data = ['python', 'java', 'golang']


@pytest.mark.parametrize('data', test_data, indirect=True)
def test_bing_sou(data, driver):
    driver.find_element(*Locator.search_text).clear()
    driver.find_element(*Locator.search_text).send_keys(data)
    driver.find_element(*Locator.search_btn).click()
