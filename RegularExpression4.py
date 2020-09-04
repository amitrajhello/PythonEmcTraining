import re

s = 'root:x:0:0:root:/root:/bin/bash'
pattern = ':'
replacement = ','
s2 = re.sub(pattern, replacement, s, count=3)
print(s2)

