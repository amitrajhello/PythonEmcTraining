"""context manager"""
with open('passwd.txt') as fp, open('passwd4.txt', 'w') as fw:
    for line in fp:
        fw.write(line + 'passwd.txt'.center(80, '-') + '\n')

print(fp.closed)
print(fw.closed)
