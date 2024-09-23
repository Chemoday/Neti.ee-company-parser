import time
from multiprocessing import Pool as ThreadPool

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# my libs
import config
from Logger import Logger
from CompanyStruct import CompanyStruct, companies
from Database import Company, save_as_csv

# Сбор только адреса сайта
def parse_neti_company_page(url):
    print('Current url', url)
    driver = Parser.create_driver()
    driver.get(url)
    time.sleep(1.5)
    try:
        # Ищем элемент с сайтом компании
        business_info_raw = driver.find_element_by_class_name('info-tabel')
        website = business_info_raw.find_element_by_class_name('fc-bi-website').text
        driver.close()
        driver.quit()
        return {'website': website}  # Возвращаем только сайт
    except Exception as e:
        print(e)
        print('Exception at: ', url)
        return None

class Parser(object):
    
    def __init__(self, debug=False):
        self.bot_url = ''
        self.debug = debug
        self.driver = Parser.create_driver()

        if self.driver:
            print('###########')
            print("Webdriver initialized successfully")

    @classmethod
    def create_driver(self):
        try:
            if config.os_type == "Windows":
                driver = webdriver.PhantomJS(executable_path='C:/Program Files (x86)/phantomjs/bin/phantomjs.exe',
                                             service_args=config.service_args,
                                             desired_capabilities=config.dcap)
            else:
                driver = webdriver.PhantomJS(service_args=config.service_args,
                                             desired_capabilities=config.dcap)
            return driver

        except AttributeError:
            print('Exception on web driver creating')
            return None

    def _parse_neti_companies_list(self, url):
        """
        Собираем названия компаний и сайты
        :param url:
        :return:
        """
        self.driver.get(url)

        actions = ActionChains(self.driver)
        elements = self.driver.find_elements_by_class_name('results-type-delay')
        for element in elements:
            actions.move_to_element_with_offset(element, xoffset=0, yoffset=100).perform()
            time.sleep(2)

        categories = url.split('/teema/')[1].split('/')
        company_category = categories[2]

        company_data_list = self.driver.find_elements_by_css_selector(".result-item.company.fc-bi-ok")
        for company_data_block in company_data_list:
            try:
                company_site_and_name = company_data_block.find_element_by_class_name('out')
                company_name = company_site_and_name.text  # Текст тега <a>
                company_website = company_site_and_name.get_attribute("href")  # URL в <a href="website">
                CompanyStruct(name=company_name, website=company_website, neti_id=None,
                              category=company_category, sub_category=None)
            except Exception as e:
                print(f"Error parsing company data: {e}")

    def fill_company_data(self):
        new_companies = [company for company in companies if
                         not Company.select().where(Company.name == company.name).exists()]
        links_list = [company.neti_url for company in new_companies]
        print('New companies len:', len(new_companies))
        company_data_list = []

        print("Total links: ", len(links_list))
        pool = ThreadPool(4)
        company_data_list = pool.map(parse_neti_company_page, links_list)
        print('Company data list:', len(company_data_list))

        for i, company in enumerate(companies):
            if company and company_data_list[i]:
                company.website = company_data_list[i]['website']  # Заполняем только URL сайта
                Company.add_company(company)

    def parse_neti_category(self, url):
        self._parse_neti_companies_list(url=url)
        self.fill_company_data()
        save_as_csv(category='Maiustused')
