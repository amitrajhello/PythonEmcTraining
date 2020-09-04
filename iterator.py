s = 'root:x:0:0:root:/root>/root:/bin/bash'

for temp in s:
    print(temp, '->', ord(temp))  # ord() is the function to print ASCII value of the character

for temp in reversed(s):
    print(temp, '->', ord(temp))
