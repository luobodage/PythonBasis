# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.id = [x for x in range(5, 15)]

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://81.70.24.116:8088/zentao/user-login.html")
        driver.find_element_by_id("account").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("123456.")
        driver.find_element_by_xpath("//div[@id='loginPanel']/header").click()
        driver.find_element_by_xpath("//div[@id='loginPanel']/div").click()
        driver.find_element_by_id("submit").click()
        driver.find_element_by_link_text(u"组织").click()
        driver.find_element_by_link_text(u"添加用户").click()
        driver.find_element_by_link_text("/").click()
        driver.find_element_by_xpath("//div[@id='dept_chosen']/div/ul/li[3]").click()
        driver.find_element_by_link_text(u"/测试部").click()
        driver.find_element_by_xpath("//div[@id='dept_chosen']/div/ul/li[2]").click()
        driver.find_element_by_id("account").click()
        driver.find_element_by_id("account").clear()
        driver.find_element_by_id("account").send_keys("luobo_test00" + str(self.id[0]))
        driver.find_element_by_id("password1").clear()
        driver.find_element_by_id("password1").send_keys("123456.")
        driver.find_element_by_id("password2").clear()
        driver.find_element_by_id("password2").send_keys("123456.")
        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("luobo")
        driver.find_element_by_id("role").click()
        Select(driver.find_element_by_id("role")).select_by_visible_text(u"研发")
        driver.find_element_by_id("role").click()
        driver.find_element_by_id("verifyPassword").click()
        driver.find_element_by_id("verifyPassword").clear()
        driver.find_element_by_id("verifyPassword").send_keys("123456.")
        driver.find_element_by_id("submit").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
