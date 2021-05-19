# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/19
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

test_username_data = ['luobochandaotest04', 'luobochandaotest05']


@pytest.fixture
def data(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def open_close_browser():
    # noinspection PyGlobalUndefined
    global driver
    driver = webdriver.Chrome()
    driver.get('http://81.70.24.116:8088/zentao/user-login-L3plbnRhby9teS5odG1s.html')
    driver.implicitly_wait(10)
    driver.maximize_window()
    # 通过id,name定位，输入文本，点击
    driver.find_element_by_id("account").send_keys("admin")
    driver.find_element_by_name("password").send_keys("123456.")
    time.sleep(1)
    driver.find_element_by_id("submit").click()
    time.sleep(3)
    print(driver.title)
    assert "我的地盘" in driver.title
    time.sleep(1)

    yield
    driver.quit()


@pytest.mark.parametrize('data', test_username_data, indirect=True)
def test_01(data):
    driver.find_element_by_link_text('组织').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="mainMenu"]/div[3]/a[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="createForm"]/table/tbody/tr[1]/td').click()
    # 选开发部
    driver.find_element_by_xpath('//*[@id="dept_chosen"]/div/ul/li[2]').click()
    driver.find_element_by_id('account').send_keys(data)
    driver.find_element_by_id('password1').send_keys('123456.')
    driver.find_element_by_id('password2').send_keys('123456.')
    driver.find_element_by_id('realname').send_keys('luobo')
    driver.find_element_by_id('verifyPassword').send_keys('123456.')
    driver.find_element_by_id('submit').click()
    time.sleep(3)
