import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import FirefoxProfile, firefox


class AfWebDriver():
    web_driver_directory = "WebDrivers"
    firefox_driver_name = "geckodriver"
    chrome_driver_name = "chromedriver"

    def get_driver_path(self, browser_name):  # TBD: make it generic for cross OS
        dirname = os.path.dirname(__file__)
        driverpath = dirname + "\\" + self.web_driver_directory + "\\" + browser_name
        print(driverpath)
        return driverpath

    def get_firefox_driver(self):
        driverpath = self.get_driver_path(self.firefox_driver_name)
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.download.dir", 'C:\\Users\\Hira.Wahid\\Downloads\\temp')
        mime_types = [
            'text/plain',
            'application/json',
            'application/vnd.ms-excel',
            'text/csv',
            'application/csv',
            'text/comma-separated-values',
            'application/download',
            'application/octet-stream',
            'binary/octet-stream',
            'application/binary',
            'application/x-unknown'
        ]
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", ",".join(mime_types))
        dirname = os.path.dirname(__file__)
        driver = webdriver.Firefox(firefox_profile=fp,executable_path=driverpath)
        return driver
    def get_chrome_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

if __name__ == '__main__':
    driver=AfWebDriver().get_chrome_driver()
