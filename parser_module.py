from bs4 import BeautifulSoup
import requests
from CompanyStruct import Company

from selenium import webdriver
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

class Parser(object):


    def get_neti_company_page_html(self, url):
        """
        Working only with http://www.neti.ee/visiitkaart/#####
        open headless browser and exececuting js element
        """
        driver.get(url)
        try:
            driver.find_element_by_link_text('Kontaktid').click()
            driver.quit()
        except:
            driver.quit()
            return None
        return(driver.page_source)

    def parse_neti_company_page(self, html):
        if not html:
            return

        html_page = BeautifulSoup(html, 'html.parser')
        #TODO add page parser




    def get_neti_companies_list(self, url):
        """
        Get companies name,urls, from category list
        accumulate companie id's
        :param url:
        :return:
        """
        driver.get(url)
        html_page = driver.page_source
        data_raw = html_page.findAll('h3', class_='name inline-block')
        for data in data_raw:
            company_raw = data.findAll('a', class_="out")
            for company in company_raw:
                company_name = company.text # Text of <a> tag
                company_website = company['href'] #content in <a href="website">
                # print("\n==============\n"
                #       "Company: {0}\n"
                #       "Website: {1}".format(company_name, company_website))
                company_obj = Company(name=company_name, website=company_website, neti_id=neti_id)
