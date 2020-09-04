# find and replacement
# inplace edit
# with time stamp
import re
from fileinput import input, filelineno
from time import time, strftime

for line in input('passwd4.txt', inplace=True, backup='.'+strftime('%Y%m%d_%H%M%S')):
    if filelineno() <= 10:
        line = re.sub(':', ',', line)

    print(line, end='')
