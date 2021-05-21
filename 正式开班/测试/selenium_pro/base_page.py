from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def enter_text(self, loc, search_data):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.click()
        ele.clear()
        ele.send_keys(search_data)

    def click_all(self, loc):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*loc))
        ele = self.driver.find_element(*loc)
        ele.click()
