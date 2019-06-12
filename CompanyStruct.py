companies = []

class CompanyStruct(object):

    def __init__(self, name, website, neti_id, category, sub_category=''):
        self.name = name
        self.website = website
        self.neti_id = neti_id
        self.category = category
        self.sub_category = sub_category
        self.neti_url = 'http://www.neti.ee/visiitkaart/' + str(neti_id)
        companies.append(self)



    def __repr__(self):
        return "Name: {name}\n" \
               "Site: {website}\n" \
               "Neti_ID: {neti_id}\n".format(name=self.name, website=self.website,
                       neti_id=self.neti_id, )

