class Person:
    """base class"""

    def __init__(self, fn, ln):  # self takes the reference of the current object
        self.fn = fn  # sets the first name of the current object
        self.ln = ln

    def get_info(self):
        print('first name:', self.fn)
        print('last name:', self.ln)


if __name__ == '__main__':  # calling main method
    p = Person('amit', 'raj')
    p.get_info()
