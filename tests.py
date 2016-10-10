from Parser import Parser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
parser = Parser()

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent

driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'], desired_capabilities=dcap)


def test_single_page_parsing():
    url = 'http://www.neti.ee/visiitkaart/80200210'
    data = parser.parse_neti_company_page(url=url)
    print(data)


url = 'http://www.neti.ee/cgi-bin/teema/MEELELAHUTUS_JA_HOBID/E-postkaardid/'
category_lst = url.split('/teema/')[1].split('/')
category = category_lst
sub_category = '-'.join(category_lst[1:])
print(sub_category)