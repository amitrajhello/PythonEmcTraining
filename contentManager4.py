# fp = open('passwd.txt')
# print(fp.read())
# fp.close()

with open('passwd.txt') as fp:  # using context manager is efficient
    print(fp.read())
