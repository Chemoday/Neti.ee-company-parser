from parser_module import Parser
from CompanyStruct import Company


from database_module import add_company, create_db, delete_db

parser = Parser()

def parse_neti():
    url = 'http://www.neti.ee/cgi-bin/teema/TERVIS/Meditsiin/Hambaravi/'
    parser.get_neti_companies_list(url=url)
    company_list = Company.COMPANY_LIST
    delete_db()
    create_db()
    for company in company_list:
        url = 'http://www.neti.ee/visiitkaart/' + str(company.neti_id)
        company_data= parser.parse_neti_company_page(url=url)
        if company_data:
            company.reg_code = company_data['reg_code']
            company.KMKR = company_data['KMKR']
            company.address = company_data['address']
            company.email = company_data['email']
            add_company(company)






def run_neti_parsing():
    parse_neti()

run_neti_parsing()