class Box:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return Box(self.size + other.size)

    def __str__(self):
        return f'[{self.__class__.__name__} size={self.size}]'

    def __mul__(self, other):
        return Box(self.size * other)


if __name__ == '__main__':
    b1 = Box(10)
    b2 = Box(20)
    b3 = Box(30)  #b1.__add__(b2)
    print(b3 * 3)

