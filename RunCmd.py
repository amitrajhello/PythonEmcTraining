import subprocess
from sys import platform
import re


if platform == 'linux':
    cmd = ['/usr/sbin/ifconfig']
elif platform == 'win32':
    cmd = ['ipconfig']

op = subprocess.check_output(cmd)
pattern = r'\b([0-9]{1-3}\.){3}[0-9]{1,3}\b'  # IPV4

for m in re.finditer(pattern, op.decode()):  # bytes into code
    print(op.decode())  # bytes into code


