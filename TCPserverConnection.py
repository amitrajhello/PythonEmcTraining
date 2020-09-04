"""tcp server"""

import socketserver
from time import ctime


class CustomRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """for each request"""
        print('recieve from: ', self.client_address)
        ts = ctime().encode()  # str into bytes
        self.request.sendall(ts)


def main():
    server_address = 'localhost', 9090
    server = socketserver.TCPServer(server_address, CustomRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
