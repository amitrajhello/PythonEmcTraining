s = 'root:x:0:0:root:/root>/root:/bin/bash'
print(s[:4])
print(s[-4:])
print(s.split(':'))
print(s.split(':')[2:5])
print(s.split(':')[:3])
print(s.split(':')[-3:])