__author__ = 'chemoday'
import datetime
import peewee

db = peewee.SqliteDatabase('company.db')


class Company(peewee.Model):
    name = peewee.TextField(default="" , primary_key=True)
    website = peewee.TextField(default="", null=True)
    reg_code = peewee.TextField(null=True)
    KMKR = peewee.TextField(null=True)
    address = peewee.TextField(default="", null=True)
    email = peewee.TextField(default="", null=True)
    class Meta:
        database = db


def create_db():
    db.connect()
    if not Company.table_exists():
        Company.create_table()
    db.close()

def delete_db():
    Company.drop_table(fail_silently=True)


def add_company(company):
    db.connect()
    row = Company(name=company.name, website=company.website, reg_code=company.reg_code,
                          KMKR=company.KMKR, address=company.address, email=company.email)
    row.save(force_insert=True)
    print("Saved: {0}".format(company.name))
    db.close()