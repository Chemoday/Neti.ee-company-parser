import os


class Logger(object):

    def __init__(self, category=None):
        self.category = category
        self.files_exist = False




    def write(self, data):
        if not self.files_exist:
            if os.path.exists('/{0}'.format(self.category)):
                os.makedirs('{0}'.format(self.category))
                print('Directory created {0}'.format(self.category))
            dir_p = os.path.join(os.getcwd()+ self.category)
            file = open(os.path.join(os.getcwd()+ "/{0}".format(self.category), "log.html"), "w+")
            file.write(data)
            file.close()
            self.files_exist = True