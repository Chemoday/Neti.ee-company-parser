from Parser import Parser
from CompanyStruct import Company
from Database import db
from Database import add_company, create_db, company_exist

parser = Parser(debug=True)

def parse_neti():
    url = 'http://www.neti.ee/cgi-bin/teema/TERVIS/Iluteenindus/'
    parser.parse_neti_companies_list(url=url)
    company_list = Company.COMPANY_LIST
    create_db()
    for company in company_list:
        if not company_exist(company):
            url = 'http://www.neti.ee/visiitkaart/' + str(company.neti_id)
            company_data= parser.parse_neti_company_page(url=url)
            if company_data:
                company.reg_code = company_data['reg_code']
                company.KMKR = company_data['KMKR']
                company.address = company_data['address']
                company.email = company_data['email']
                add_company(company)
    db.close()





def run_neti_parsing():
    create_db()
    parse_neti()

    print("Parsing is done")

run_neti_parsing()