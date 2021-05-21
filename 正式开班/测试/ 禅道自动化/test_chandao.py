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
from login_page import Login_page
from add_user import Add_user

login_username = ['admin']
login_password = ['123456.']
username_list = ['luobodarling003', 'yuyudarling003', 'baby003', 'darling003']


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.get('http://81.70.24.116:8088/zentao/user-login-L3plbnRhby9teS5odG1s.html')
    page = Login_page(driver)
    page.main_login(login_username, login_password)
    time.sleep(1)
    yield driver
    driver.quit()


@pytest.mark.parametrize('data', username_list)
def test_add01(driver, data):
    username_page = Add_user(driver)
    username_page.main_add_user(data, login_password)
    # driver.find_element_by_id('bysearchTab').click()
    # time.sleep(1)
    # driver.find_element_by_link_text('真实姓名').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="field1_chosen"]/div/ul/li[4]').click()
    # time.sleep(1)
    # driver.find_element_by_id('value1').clear()
    # driver.find_element_by_id('value1').send_keys(data)
    # time.sleep(1)
    # driver.find_element_by_id('submit').click()
    # time.sleep(2)
    # assert data in driver.page_source
    assert '组织视图首页' in driver.title
