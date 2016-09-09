from bs4 import BeautifulSoup
import requests
from CompanyStruct import Company

from selenium import webdriver
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

class Parser(object):


    def __get_neti_company_page_html(self, url):
        """
        Working only with http://www.neti.ee/visiitkaart/#####
        open headless browser, execute js element
        and returning full html page source ( with info under js script )
        """
        driver.get(url)
        try:
            driver.find_element_by_link_text('Kontaktid').click()
            driver.quit()
        except:
            driver.quit()
            return None
        return(driver.page_source)

    def parse_neti_company_page(self, url):
        html = self.__get_neti_company_page_html(url=url)
        if not html:
            return None
        html = BeautifulSoup(html, 'html.parser')
        company_data = {}

        return company_data
        #TODO add page parser




    def get_neti_companies_list(self, url):
        """
        Get companies name,urls, from category list
        accumulate companie id's
        :param url:
        :return:
        """
        driver.get(url)
        html_page = BeautifulSoup(driver.page_source, 'html.parser')
        company_data_list = html_page.findAll('li', class_='result-item company fc-bi-ok')
        for company_data_block in company_data_list:
            company_site_and_name = company_data_block.find('a', class_="out")
            company_name = company_site_and_name.getText() # Text of <a> tag
            company_website = company_site_and_name['href'] #content in <a href="website">

            company_neti_id_raw = company_data_block.find('div', class_='real-expand fc-tabs')
            company_neti_id = company_neti_id_raw['data-bizinfo-reg-code']

            # print("\n==============\n"
            #       "Company: {0}\n"
            #       "Website: {1}".format(company_name, company_website))
            Company(name=company_name, website=company_website, neti_id=company_neti_id)
