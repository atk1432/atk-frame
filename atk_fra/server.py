from http.server import BaseHTTPRequestHandler, HTTPServer

URLS = {}

def start(url, func):
    URLS[url] = func
    return Server
        

class Server(BaseHTTPRequestHandler):
    """ Process request and response """

    def get_url(self):
        if URLS.get(self.path, False):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
           # if URLS[self.path].__name__ == 'loader':
            self.wfile.write(bytes("<html><head><title>My framework</title></head><body>", "utf-8"))
            self.wfile.write(bytes("{}".format(URLS[self.path]()), "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


    def do_GET(self):
        self.get_url()
    
    
        

