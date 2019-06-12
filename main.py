from Parser import Parser
from Database import create_db
from datetime import datetime


parser = Parser(debug=True)

def parse_neti():
    startTime = datetime.now()
    create_db()
    # url = 'http://www.neti.ee/cgi-bin/teema/TERVIS/Meditsiin/'
    url = 'https://www.neti.ee/cgi-bin/teema/ARI/Toidukaubad/Maiustused/'
    parser.parse_neti_category(url=url)
    print("Parsing is done")
    execution_time = datetime.now() - startTime
    print("Execution time is :{0}".format(execution_time))
parse_neti()