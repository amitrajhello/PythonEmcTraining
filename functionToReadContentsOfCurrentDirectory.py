import os


def ls(dir_path='.'):
    for item in os.listdir(dir_path):
        print(item)

ls('.')
print()
ls('..')



