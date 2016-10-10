#python lib
import time
#imported libs
from bs4 import BeautifulSoup

#my libs
from Logger import Logger
from CompanyStruct import Company


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#To change user_agent
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent



class Parser(object):

    def __init__(self, debug=False):
            self.debug = debug

    def __get_neti_company_page_html(self, url):
        """
        Working only with http://www.neti.ee/visiitkaart/#####
        open headless browser, execute js element
        and returning full html page source ( with info under js script )
        """
        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any','--load-images=no']
                                 , desired_capabilities=dcap, port=8080,)
        driver.get(url)
        try:
            driver.find_element_by_link_text('Kontaktid').click()
            time.sleep(0.5)
            page_source = driver.page_source
            driver.quit()
            return page_source
        except:
            driver.quit()
            return None


    def parse_neti_company_page(self, url):
        html = self.__get_neti_company_page_html(url=url)
        if not html:
            print("None was returned | if not html")
            return None
        html = BeautifulSoup(html, 'html.parser')
        try:
            business_info_raw = html.find('table', class_='info-tabel')
            reg_code = business_info_raw.find('td', class_='fc-bi-regcode-value').getText()
            KMKR = business_info_raw.find('td', class_='fc-bi-kmkr-value').getText()
            address = business_info_raw.find('td', class_='fc-bi-address-value').getText()
            email = business_info_raw.find('td', class_='fc-bi-contact-value').getText()
            company_data = {
                'reg_code': reg_code,
                'KMKR': KMKR,
                'address': address,
                'email': email
            }
            return company_data
        except:
            print("Error on page scraping")
            return None




    def parse_neti_companies_list(self, url):
        """
        Get companies name,urls, from category list
        accumulate companies id's
        :param url:
        :return:
        """
        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any','--load-images=no']
                                  , desired_capabilities=dcap, port=8080)
        driver.get(url)

        # actions = ActionChains(driver)
        # elements = driver.find_elements_by_class_name('results-type-delay')
        # for element in elements:
        #     actions.move_to_element_with_offset(element, xoffset=0, yoffset=100).perform()
        #     time.sleep(2)


        html = driver.page_source
        if self.debug:
            logger = Logger(category='Category')
            logger.write(data=html)
        html_page = BeautifulSoup(html, 'html.parser')
        driver.quit()
        category_lst = url.split('/teema/')[1].split('/')
        company_category = category_lst[1]
        if len(category_lst) > 1:
            company_sub_category = '-'.join(category_lst[1:])
        else:
            company_sub_category  = ''
        company_data_list = html_page.findAll('li', class_='result-item company fc-bi-ok')
        for company_data_block in company_data_list:
            company_site_and_name = company_data_block.find('a', class_="out")
            company_name = company_site_and_name.getText() # Text of <a> tag
            company_website = company_site_and_name['href'] #  content in <a href="website">

            company_neti_id_raw = company_data_block.find('div', class_='real-expand fc-tabs')
            company_neti_id = company_neti_id_raw['data-bizinfo-reg-code']

            #  print("\n==============\n"
            #       "Company: {0}\n"
            #       "Website: {1}".format(company_name, company_website))
            Company(name=company_name, website=company_website, neti_id=company_neti_id,
                    category=company_category, sub_category=company_sub_category)
