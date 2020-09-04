from inheritence import Person


class Employee(Person):
    """Employee class extends to class Person"""

    def __init__(self, eid, fn, ln):
        self.eid = eid
        super().__init__(fn, ln)  # invoke the overridden method

    def get_info(self):
        print('employee id:', self.eid)
        super().get_info()


if __name__ == '__main__':  # calling main method
    e = Employee('3242', 'Amit', 'Singh')
    e.get_info()
