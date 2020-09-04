from directoryListingExercise import DirectoryListing
from json import dump


class DirectoryListingToJason(DirectoryListing):
    def to_json(self, json_file):
        try:
            dump(self.container, open(json_file, 'w'), indent=2)
        except IOError as err:
            print(err)


if __name__ == '__main__':
    DirectoryListingToJason(r'C:\Users\raja6\PycharmProjects\emc\python advanced').to_json('tmp.json')

