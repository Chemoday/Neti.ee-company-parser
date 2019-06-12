#python lib
import time
from multiprocessing import Pool as ThreadPool
#imported libs

#my libs
import config
from Logger import Logger
from CompanyStruct import CompanyStruct, companies
from Database import Company, save_as_csv

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def parse_neti_company_page(url):
    #Moved out to fix mutiprocessing problem - cant pickle local object
    print('Current url', url)
    driver = Parser.create_driver()
    driver.get(url)
    time.sleep(1.5)
    try:
        business_info_raw = driver.find_element_by_class_name('info-tabel')
        reg_code = business_info_raw.find_element_by_class_name('fc-bi-regcode-value').text
        KMKR = business_info_raw.find_element_by_class_name('fc-bi-kmkr-value').text
        address = business_info_raw.find_element_by_class_name('fc-bi-address-value').text
        email = business_info_raw.find_element_by_class_name('fc-bi-contact-value').text
        company_data = {
            'reg_code': reg_code,
            'KMKR': KMKR,
            'address': address,
            'email': email
        }
        driver.close()
        driver.quit()
        return company_data
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
            #driver.get(config.url)
            return driver

        except AttributeError:
            print('Exception on web driver creating')
            return None




    def _parse_neti_companies_list(self, url):
        """
        Get companies name,urls, from category list
        accumulate companies id's
        :param url:
        :return:
        """
        self.driver.get(url)

        actions = ActionChains(self.driver)
        elements = self.driver.find_elements_by_class_name('results-type-delay')
        for element in elements:
            actions.move_to_element_with_offset(element, xoffset=0, yoffset=100).perform()
            time.sleep(2)


        # if self.debug:
        #     logger = Logger(category='Category')
        #     logger.write(data=html)

        categories = url.split('/teema/')[1].split('/')

        company_category = categories[2]

        company_data_list = self.driver.find_elements_by_css_selector(".result-item.company.fc-bi-ok")
        for company_data_block in company_data_list:
            try:
                company_sub_category = company_data_block.find_element_by_css_selector('.result-text.inline-block').text #description
            except Exception as e:
                company_sub_category = ''
            company_site_and_name = company_data_block.find_element_by_class_name('out')
            company_name = company_site_and_name.text # Text of <a> tag
            company_website = company_site_and_name.get_attribute("href") #  content in <a href="website">

            company_neti_id_raw = company_data_block.find_element_by_css_selector('.real-expand.fc-tabs.movebanner_true')
            company_neti_id = company_neti_id_raw.get_attribute('data-bizinfo-reg-code')

            #  print("\n==============\n"
            #       "Company: {0}\n"
            #       "Website: {1}".format(company_name, company_website))
            CompanyStruct(name=company_name, website=company_website, neti_id=company_neti_id,
                          category=company_category, sub_category=company_sub_category)

    def fill_company_data(self):
        new_companies = [company for company in companies if
                         not Company.select().where(Company.name == company.name).exists()]
        links_list = [company.neti_url for company in new_companies]
        print('New companies len:', len(new_companies))
        company_data_list = []


        # for link in links_list:
        #     company_data_list.append(parse_neti_company_page(self.driver, link))
        print("Total links: ", len(links_list))
        pool = ThreadPool(4)
        company_data_list = pool.map(parse_neti_company_page, links_list)
        print('Company data list:', len(company_data_list))

        for i, company in enumerate(companies):
            if company:
                company.reg_code = company_data_list[i]['reg_code']
                company.KMKR = company_data_list[i]['KMKR']
                company.address = company_data_list[i]['address']
                company.email = company_data_list[i]['email']
                Company.add_company(company)



        # for company in Company.COMPANY_LIST:
        #     if not company_exist(company):
        #         url = 'http://www.neti.ee/visiitkaart/' + str(company.neti_id)
        #         company_data = self.parse_neti_company_page(url=url)
        #         if company_data:
        #             company.reg_code = company_data['reg_code']
        #             company.KMKR = company_data['KMKR']
        #             company.address = company_data['address']
        #             company.email = company_data['email']
        #             add_company(company)

    def parse_neti_category(self, url):
        self._parse_neti_companies_list(url=url)

        self.fill_company_data()
        save_as_csv(category='Maiustused')

