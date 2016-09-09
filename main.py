from parser_module import Parser
from CompanyStruct import Company

parser = Parser()

def parse_neti():
    url = 'http://www.neti.ee/cgi-bin/teema/TERVIS/Meditsiin/Hambaravi/'

    parser.get_neti_companies_list(url=url)
    for company in Company.COMPANY_LIST:
        company_data = parser.parse_neti_company_page(url=url)
        if company_data:
            company.reg_code = company_data['reg_code']
            company.KMKR = company_data['KMKR']
            company.address = company_data['address']
            company.email = company_data['email']
    print('Done')


def db_add_neti():
    for company in Company.COMPANY_LIST:
        pass
    #TODO add to DB




def run_neti_parsing():
    parse_neti()
    db_add_neti()
