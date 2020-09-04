from os import listdir
from os.path import join, isfile, isdir, getsize, getmtime
from time import ctime


dir_path = r'C:\Users\raja6\PycharmProjects\emc\python advanced'
item = listdir(dir_path)[0]
abs_path = join(dir_path, item)
print(abs_path)
print()
print(isdir(abs_path))
print(isfile(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))

