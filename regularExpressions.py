import re

s = 'the pythonscripting and the perl scripting'
pattern = 'P.+?N'  # non-greedy

m = re.search(pattern, s, re.I)

if m:
    print(m)
    print('match string:', m.group())
    print(m.start())
    print(m.end())

else:
    print('failed to match')

