from Parser import Parser
from multiprocessing import Pool as ThreadPool
from Database import db
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
parser = Parser()


def test_single_page_parsing():
    url_list = ['http://www.neti.ee/visiitkaart/80329197','http://www.neti.ee/visiitkaart/32917135']
    pool = ThreadPool(4)
    company_data_list = pool.map(parser.parse_neti_company_page, url_list)
    print(company_data_list)
    db

test_single_page_parsing()