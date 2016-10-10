__author__ = 'chemoday'
import datetime
import peewee
db = peewee.SqliteDatabase('company.db')

class Utils(object):
    total_parsed=0

class Company(peewee.Model):
    name = peewee.TextField(default="" , primary_key=True)
    website = peewee.TextField(default="", null=True)
    reg_code = peewee.TextField(null=True)
    KMKR = peewee.TextField(null=True)
    address = peewee.TextField(default="", null=True)
    email = peewee.TextField(default="", null=True)
    category = peewee.TextField(default="", null=False)
    sub_category = peewee.TextField(default="", null=True)
    class Meta:
        database = db


def create_db():
    db.connect()
    if not Company.table_exists():
        Company.create_table()

def delete_db():
    Company.drop_table(fail_silently=True)

def company_exist(company):
    try:
        company = Company.get(Company.name==company.name)
        return True
    except Company.DoesNotExist:
        return False

def add_company(company):

    try:
        row = Company(name=company.name, website=company.website, reg_code=company.reg_code,
                              KMKR=company.KMKR, address=company.address, email=company.email,
                              category=company.category, sub_category=company.sub_category)
        row.save(force_insert=True)
        Utils.total_parsed+=1
        print("Saved: {0}| Session total:{1}".format(company.name, Utils.total_parsed))
    except peewee.IntegrityError:
        print("Eror with: {0}".format(company.name))

