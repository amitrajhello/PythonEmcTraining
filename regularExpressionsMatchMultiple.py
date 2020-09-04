import re

s = 'the python scripting and the perl scripting'
pattern = 'P.+?N'  # non-greedy

for m in re.finditer(pattern, s, re.I):
    print(m.group())
    print(m.span())
    print()



