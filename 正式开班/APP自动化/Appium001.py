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
import time

from appium import webdriver

# 初始化参数
server = r'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '6.0.1',  # 手机安卓版本
    'deviceName': '127.0.0.1:7555',  # 设备名，安卓手机可以随意填写
    'appPackage': 'io.appium.android.apis',  # 启动APP Package名称
    'appActivity': '.ApiDemos',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True
}
driver = webdriver.Remote(server, desired_caps)  # 连接手机和APP
el1 = driver.find_element_by_accessibility_id("App")
el1.click()
driver.back()
el2 = driver.find_element_by_accessibility_id("OS")
el2.click()
el3 = driver.find_element_by_accessibility_id("SMS Messaging")
el3.click()
driver.back()
driver.back()
driver.back()
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[11]")
el4.click()

print(driver.current_package)
print(driver.current_activity)
driver.quit()
