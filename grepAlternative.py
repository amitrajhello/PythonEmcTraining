""" DEmo to search a pattern in a files"""
import re
from fileinput import input, filelineno, filename


class GrepMe:
    def __init__(self, pattern, *args):
        self.pattern = pattern
        self.file_names = args
        self.do_match()

    def do_match(self):
        for line in input(self.file_names):
            if re.search(self.pattern, line, re.I):
                print(f'{filename()}:{filelineno()}:{line}', end='')


if __name__ == '__main__':
    GrepMe('root', r'C:\Users\raja6\Desktop\study\emc python training\passwd.txt',
           r'C:\Users\raja6\Desktop\study\emc python training\passwd2.txt')

