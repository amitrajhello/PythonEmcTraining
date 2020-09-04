class Alpha:
    def pprint(self):
        print('pprint from class Alpha')


class Beta:
    def pprint(self):
        print('pprint from the class Beta')


class Charlie(Alpha, Beta):
    def pprint(self):
        super().pprint()  # super() method runs the medthod from first inherited class
        Alpha.pprint(self)
        Beta.pprint(self)


if __name__ == '__main__':
    Charlie().pprint()
