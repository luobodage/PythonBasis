# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/18
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
import unittest

from selenium import webdriver


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        print('打开浏览器！')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"

    def test_01untitled_test_case(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        driver.save_screenshot('百度首页截图.png')
        print('截图成功！')
        # 是否可见
        print('新闻按钮是否可见：', driver.find_element_by_link_text('新闻').is_displayed())
        # 是否可选
        print('新闻按钮是否可选：', driver.find_element_by_link_text('新闻').is_enabled())
        # 是否可用
        print('新闻按钮是否可用：', driver.find_element_by_link_text('新闻').is_selected())

    def test_02untitled_test_case(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        driver.save_screenshot('百度首页截图1.png')
        print('截图成功！')
        # 是否可见
        print('地图按钮是否可见：', driver.find_element_by_link_text('地图').is_displayed())
        # 是否可选
        print('地图按钮是否可选：', driver.find_element_by_link_text('地图').is_enabled())
        # 是否可用
        print('地图按钮是否可用：', driver.find_element_by_link_text('地图').is_selected())

    def tearDown(self):
        print('关闭浏览器！')
        driver = self.driver
        driver.quit()


if __name__ == "__main__":
    unittest.main()
