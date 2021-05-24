# -*- coding: UTF-8 -*-

# author: luoboovo
# contact: fuyu16032001@gmail.com
# datetime: 2021/05/24
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
import allure

'''
Import allure
功能上加@allure.feature(‘功能名称’)
子功能上加@allure.story(‘子功能名称’)
步骤上加@allure.step(‘步骤细节’)
'''


@allure.feature("购物功能")
class TestShoppingDemo(object):
    @allure.step("1、登陆的数据准备")
    @pytest.fixture()
    def data(self):
        self.data = [1, 2, 3]

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step("进行登陆")
    @allure.story("登陆")
    def test_login(self, data):
        print('登陆', data)

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("添加购物车")
    def test_cart(self):
        with allure.step("1、搜索商品"):
            print('搜索商品')
            allure.attach(body="<html><body>你已经到达一个非法页面</body></html>", name='',
                          attachment_type=allure.attachment_type.HTML)
            # print("错误html")
        with allure.step("2、添加购物车"):
            print('添加购物车')

        allure.attach.file("1.gif", "添加成功", allure.attachment_type.PNG)
        print("driver.sava_shootpicture("")")
        with allure.step("3、查看购物车并判断是否添加成功"):
            print('查看购物车')
            allure.attach('期望结果', '添加购物车成功')
            allure.attach('实际结果', '添加购物车失败')
            assert 1 == 1

    @allure.testcase("http://81.70.24.116:8088/zentao/bug-view-27.html", "支付测试用例")
    @allure.link("http://www.bing.com", "bug的信息")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("支付")
    def test_pay(self):
        print('支付')
