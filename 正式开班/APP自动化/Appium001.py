# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/07
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
# 导入webdriver
from appium import webdriver

# 初始化参数
server = r'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '6.0.1',  # 手机安卓版本
    'deviceName': '127.0.0.1:7555',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.youdao.note',  # 启动APP Package名称
    'appActivity': '.activity2.MainActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法

}
driver = webdriver.Remote(server, desired_caps)  # 连接手机和APP
driver.find_element_by_id("com.youdao.note:id/add_note").click()
print(driver.current_package)
print(driver.current_activity)
driver.quit()
