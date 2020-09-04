class HeadAndTail:
    def __init__(self, file_name):
        pass

    def __rshift__(self, other):
        with open('passwd.txt') as f:
            content = f.readlines()
            content1 = [x.strip() for x in content]
            return content1[:5]

    def __lshift__(self, other):
        with open('passwd.txt') as f:
            content = f.readlines()
            content1 = [x.strip() for x in content]
            return content1[-5:]


if __name__ == '__main__':
    ht = HeadAndTail('passwd.txt')
    print(ht >> 5)  # the last 5 lines from the file; tail -5 passwd
    print()
    print(ht << 5)
