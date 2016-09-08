from parser_module import Parser
from CompanyStruct import Company
parser = Parser()


def parse_neti():
    url = 'http://www.neti.ee/cgi-bin/teema/TERVIS/Meditsiin/Hambaravi/'

    parser.get_neti_companies_list(url=url)
    for company in Company.COMPANY_LIST:
        #TODO add code
        pass

parser.get_html('http://www.neti.ee/visiitkaart/80145066')
