import datetime
import urllib.request

import xlrd
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from Webdriver_functions import AfWebDriver


class Test():
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        pass
    def test_internet_connectivity(self):
        try:
            urllib.request.urlopen("http://www.google.com")
            skip_all = True
        except:
            skip_all = False
            pytest.exit('No connectivity')
        print(skip_all)
    def test_further(self):
        driver = AfWebDriver().get_chrome_driver()
        driver.implicitly_wait(10)
        wb = xlrd.open_workbook("qaautomation.xlsx")
        sheet = wb.sheet_by_index(0)
        print(sheet.cell_value(0, 1))
        driver.get(sheet.cell_value(0, 1))
        driver.find_element_by_xpath("//input[@type='text']").send_keys(sheet.cell_value(1, 1))
        driver.find_element_by_xpath("//input[@type='text']").send_keys(u'\ue007')
        time.sleep(2)
        link=driver.find_element_by_xpath("//*[contains(text(),'After Life (TV Series 2019– ) - IMDb')]")
        actionChains = ActionChains(driver)
        actionChains.context_click(link).perform()
        ac=driver.switch_to.active_element
        actionChains.key_down(Keys.CONTROL).click(ac).key_up(Keys.CONTROL).perform()
        main_window = driver.current_window_handle
        driver.switch_to.window(driver.window_handles[-1])
        link=driver.find_element_by_xpath("//*[contains(text(),'See full cast')]").click()
        time.sleep(5)
        for i in driver.find_elements_by_xpath("//table[@class='cast_list']//a"):
            print(i.get_attribute('innerHTML'))
        time.sleep(5)

        pass