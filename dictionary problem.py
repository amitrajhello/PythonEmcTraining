import csv
import pprint

shells_count ={}

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    print(row)

print()

for row in csv.reader(open('passwd.txt'), delimiter=':'):
    shell = row[-1]
    shells_count[shell] = shells_count.get(shell,0)+1

pprint.pprint(shells_count)

for name, count in shells_count.items():
    print('{:>20} : {}'.format(name, count))

