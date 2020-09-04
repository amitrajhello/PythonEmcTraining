items = [2.2, 'pam', 3.4, 'allen', .98, 'allen', 'nick', 1, 2, 'allen', 3, 4, 'allen']

print(items)
print()

while 'allen' in items:    # membership test operator 'in'
    items.remove('allen')

print(items)
