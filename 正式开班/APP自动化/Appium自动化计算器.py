# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/28
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
from appium import webdriver

server = r'http://localhost:4723/wd/hub'
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '6.0.1',  # 手机安卓版本
    'deviceName': '127.0.0.1:7555',  # 设备名，安卓手机可以随意填写
    'appPackage': 'com.youdao.calculator',  # 启动APP Package名称
    'appActivity': '.activities.MainActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True
}


@pytest.fixture()
def data(request):
    return request.param


@pytest.fixture(scope='module', autouse=True)
def open_close_app():
    # noinspection PyGlobalUndefined
    global driver
    driver = webdriver.Remote(server, desired_caps)
    time.sleep(1)
    yield driver
    driver.quit()


@pytest.mark.parametrize('data', [10, 15, 20, 30], indirect=True)
def test_jisuanqi_add(data):
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout"
        "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
        ".LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout["
        "3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout["
        "7]/android.widget.FrameLayout/android.widget.ImageView").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout"
        "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
        ".LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout["
        "3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout["
        "20]/android.widget.FrameLayout/android.widget.ImageView").click()
    time.sleep(1)
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout"
        "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
        ".LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout["
        "3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout["
        "8]/android.widget.FrameLayout/android.widget.ImageView").click()
    time.sleep(2)

    # driver.find_element_by_id('resultOpIcon').click()
    driver.tap([(129, 227)])
    time.sleep(2)
    content = driver.find_element_by_id("com.youdao.calculator:id/tv_keyclipboard").get_attribute('text')
    print(content)
    driver.tap([(660, 675)])
    driver.tap([(660, 675)])
    driver.tap([(660, 675)])
    assert data == int(content)


