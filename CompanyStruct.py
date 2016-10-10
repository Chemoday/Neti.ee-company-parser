class Company(object):
    COMPANY_LIST = []
    reg_code = None
    KMKR = None
    address = None
    email = None



    def __init__(self, name, website, neti_id, category, sub_category=''):
        self.name = name
        self.website = website
        self.neti_id = neti_id
        self.category = category
        self.sub_category = sub_category
        Company.COMPANY_LIST.append(self)


    def __repr__(self):
        return "Name: {name}\n" \
               "Site: {website}\n" \
               "Neti_ID: {neti_id}\n" \
               "Reg_Code:{code}\n" \
               "Address: {address}\n" \
               "Email: {email}\n" \
               .format(name=self.name,code=self.reg_code,
                                     address=self.address, email=self.email,
                                     website=self.website, neti_id = self.neti_id )

