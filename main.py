from parser_module import Parser


class Company(object):
    reg_code = ''
    address = ''
    email = ''
    link = ''
    KMKR = ''


    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return "Name: {name}\n" \
               "Reg_Code:{code}\n" \
               "Address: {address}\n" \
               "Email: {email}\n" \
               "Page: {link}".format(name=self.name,code=self.reg_code,
                                     address=self.address, email=self.email,
                                     link=self.link )

parser = Parser()
parser.get_html('http://www.neti.ee/visiitkaart/80145066')
