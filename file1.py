'''demo for file read'''
fp = open('passwd.txt')

print(fp)

for temp in fp:
    print(temp, end='')

fp.close()


