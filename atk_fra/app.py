from http.server import BaseHTTPRequestHandler, HTTPServer
import server
import sys
from utilities import loader

HOSTNAME = 'localhost'
PORT = 8080

class App:

    """
        App is center to process request
    """
    @staticmethod
    def listen(url, func):
        s = server.start(url, func)     

        web_server = HTTPServer((HOSTNAME, PORT), s)
        link = web_server.server_address
        print('Server started at: http://{}:{}'.format(link[0], link[1])) 
        try:
            web_server.serve_forever()
        except KeyboardInterrupt:
            web_server.server_close()
            sys.exit()


if __name__ == '__main__':
    def start():
        return loader('templates/index.html')

    App.listen('/', start)
