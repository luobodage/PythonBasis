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
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test_username_data = ['python', 'java', 'golang', 'ruby']


@pytest.fixture
def data(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def open_close_browser():
    # noinspection PyGlobalUndefined
    global driver
    driver = webdriver.Chrome()
    driver.get('https://cn.bing.com/')
    time.sleep(1)
    yield
    driver.quit()


@pytest.mark.parametrize('data', test_username_data, indirect=True)
def test_01(data):
    driver.find_element_by_id('sb_form_q').clear()
    driver.find_element_by_id('sb_form_q').send_keys(data)
    driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER)
    time.sleep(1)
    html = driver.find_element_by_xpath('//*').get_attribute("innerHTML")
    time.sleep(1)
    with open(f'bing_html/{data}_bing.html', 'w', encoding='utf8') as f:
        f.write(html)
