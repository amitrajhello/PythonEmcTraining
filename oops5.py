"""
PackageManager

name
version

__init__()
get_information()

"""


class PackageManager:
    def __init__(self, name, version):
        self.__name = name  # private attribute
        self.version = version

    def wrapper(self):
        """public method"""
        self.__get_information()

    def __get_information(self):
        """private method"""
        print('name:', self.__name)
        print('version:', self.version)


if __name__ == '__main__':
    pm = PackageManager('pip', '2.2.18')
    pm.wrapper()
