from zipfile import ZipFile
from glob import glob


class MakeArchive:
    def __init__(self, archive_name, *args):
        self.archive_name = archive_name
        self.archive_content = args
        self.save()

    def save(self):
        with ZipFile(self.archive_name, mode='w') as zf:
            for item in self.archive_content:
                zf.write(item)
                print(f'{item}: added')


if __name__ == '__main__':
    MakeArchive(r'C:\Users\raja6\PycharmProjects\emc\python advanced\pdfs.zip',
                *glob(r'C:\Users\raja6\PycharmProjects\emc\python advanced\*.py'))
