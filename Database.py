__author__ = 'chemoday'
import datetime
import peewee

db = peewee.SqliteDatabase('company.db')
db.connect()

class Utils(object):
    total_parsed=0

class Company(peewee.Model):
    total_saved = 0

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

    @staticmethod
    def add_company(company):
        try:
            Company.insert(name=company.name, website=company.website, reg_code=company.reg_code,
                           KMKR=company.KMKR, address=company.address, email=company.email,
                           category=company.category, sub_category=company.sub_category).execute()
            Utils.total_parsed+= 1
            print("Saved: {0} | Session total:{1}".format(company.name, Utils.total_parsed))
        except peewee.IntegrityError:
            print("Eror with: {0}".format(company.name))

def create_db():
    if not Company.table_exists():
        Company.create_table()

def delete_db():
    Company.drop_table(fail_silently=True)

def company_exist(company):
    try:
        company = Company.get(Company.name==company.name)
        return True
    except Company.DoesNotExist:
        print('Company:{0} NOT EXIST| email:{1}'.format(company.name, company.email))
        return False



def save_as_csv(category):
    import pandas as pd
    connection = db.connection()
    sql = Company.select().where(Company.category == category).sql()
    df = pd.read_sql(sql[0], connection, params=sql[1])
    df.to_csv('csv/{0}.csv'.format(category))