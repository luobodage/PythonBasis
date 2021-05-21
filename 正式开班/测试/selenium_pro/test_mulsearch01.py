from selenium import webdriver
import pytest

from .seacrh_page import BasePage, SearchPage


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://cn.bing.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize('search', ['python', 'pytest', 'fiddler', 'selenium'])
def test_bing_sou(driver, search):
    page = SearchPage(driver)
    page.main_search(search)
    assert search in driver.page_source
# 关闭浏览器，释放资源
