fp = open('passwd.txt')

print(fp)
list1 = []

for temp in fp:
    list1.append(fp[0])
        
print(list1)
fp.close()
