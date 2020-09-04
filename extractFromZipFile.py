from zipfile import ZipFile
from os.path import isdir
from os import mkdir


def extract_archive(archive_name, target_dir):
    try:
        if not isdir(target_dir):
            mkdir(target_dir)

        with ZipFile(archive_name, mode='r') as zf:
            zf.extractall(target_dir)
    except FileNotFoundError as err:
        print(err)
    except PermissionError as err:
        print(err)


if __name__ == '__main__':
    extract_archive('pdfs.zip', r'C:\Users\raja6\PycharmProjects\emc\extracted')

