items = [2.2, 'pam', 3.4, 'allen', .98, 'nick', 1, 2, 3, 4]

print(items)
print()

del items[:3]   # first 3 items
print(items)
print()

del items[-4:-2]   # 4th and 3rd items from the end of the list
print(items)
print()

del items[-3:]    # last 3
print(items)
print()

