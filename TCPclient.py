"""tcp"""

import socket

try:
    server_address = 'localhost', 9090
    sock = socket.socket()
    sock.connect(server_address)
    payload = sock.recv(1024)
    print(payload.decode())     # bytes to str
finally:
    sock.close()
