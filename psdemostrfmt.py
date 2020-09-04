"""demo for the str fmt"""
# {:fmt-str}

name, age, gender = 'sarah', 3, 'female'

print('|{}|{}|{}|'.format(name, age, gender))
print('|{:>22}|{:>9}|{:>16}|'.format(name, age, gender))
print('|{:<22}|{:<9}|{:<16}|'.format(name, age, gender))
print('|{:^22}|{:^9}|{:^16}|'.format(name, age, gender))
print('|{:22}|{:9}|{:16}|'.format(name, age, gender))
print('|{:22}|{:9.2f}|{:16}|'.format(name, age, gender))
