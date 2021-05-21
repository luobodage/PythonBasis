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
from selenium.webdriver.common.by import By
import random


class Locator:
    login_user = (By.ID, 'account')
    login_password = (By.NAME, 'password')
    login_submit = (By.ID, 'submit')
    organization_submit = (By.LINK_TEXT, '组织')
    add_user_submit = (By.XPATH, '//*[@id="mainMenu"]/div[3]/a[2]')
    department_submit = (By.XPATH, '//*[@id="createForm"]/table/tbody/tr[1]/td')
    department = (By.XPATH, f'//*[@id="dept_chosen"]/div/ul/li[{random.choice(range(2, 6))}]')
    # department = (By.XPATH, '//*[@id="dept_chosen"]/div/ul/li[2]')
    user_name = (By.ID, 'account')
    password_one = (By.ID, 'password1')
    password_two = (By.ID, 'password2')
    realname = (By.ID, 'realname')
    verify_Password = (By.ID, "verifyPassword")
    add_submit = (By.ID, 'submit')
