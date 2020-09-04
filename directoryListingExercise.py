from os import listdir
from os.path import join, isfile, getsize, getmtime
from time import ctime
from pprint import pprint as pp


class DirectoryListing:
    def __init__(self, *args):
        self.directories = args
        self.container = {}
        self.read_directories()

    def read_directories(self):
        for dir_name in self.directories:
            for item in listdir(dir_name):
                abs_path = join(dir_name, item)

                if isfile(abs_path):
                    list_of_file_properties = [getsize(abs_path), ctime(getmtime(abs_path))]
                    self.container.setdefault(dir_name, {})[item] = list_of_file_properties  # set +get
                    """
                    temp = self.container.setdefault(dir_name, {})
                    temp[item] = list_of_file_properties  
                    """


if __name__ == '__main__':
    dl = DirectoryListing(r'C:\Users\raja6\PycharmProjects\emc\python advanced')
    pp(dl.container)

"""
{
    'd1':{
        'f1'= [size, mtime]
        }, ....
}
"""
