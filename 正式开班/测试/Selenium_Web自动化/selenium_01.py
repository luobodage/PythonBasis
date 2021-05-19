# -*- coding: UTF-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/17
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

driver = webdriver.Chrome()
driver.get("http://81.70.24.116:8088/zentao/user-login.html")
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

driver.find_element_by_link_text('组织').click()
time.sleep(1)
# 点击添加
driver.find_element_by_xpath('//*[@id="mainMenu"]/div[3]/a[2]').click()
time.sleep(1)
# 选中下拉框
driver.find_element_by_xpath('//*[@id="createForm"]/table/tbody/tr[1]/td').click()
# 选开发部
driver.find_element_by_xpath('//*[@id="dept_chosen"]/div/ul/li[2]').click()
# driver.quit()
html = driver.find_element_by_xpath('//*').get_attribute("innerHTML")
print(html)
