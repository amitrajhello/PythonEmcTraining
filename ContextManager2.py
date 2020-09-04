"""context manager"""
with open('passwd.txt') as fp, open('passwd4.txt','w') as fw:
    fw.write(fp.read())

print(fp.closed)
print(fw.closed)
