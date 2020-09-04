s = 'root,x,0,0,root,/root,/bin/bash'

items = s.split(',')
print(items)
print()
print(s.split(',')[0])
print()
print(s.split(',')[1:])
print()

for item in s.split(',')[1:]:
    print(item)
