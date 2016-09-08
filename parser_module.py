import bs4
import time

from selenium import webdriver
driver = webdriver.PhantomJS()

class Parser(object):


    @staticmethod
    def get_html(url):
        driver.get(url)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/ul/li/div[2]/div[2]/a')
        print(driver.page_source)
        driver.quit()