from http.server import BaseHTTPRequestHandler, HTTPServer

URLS = {}

def start(url, func):
    URLS[url] = func
    return Server
        

class Server(BaseHTTPRequestHandler):
    """ Process request and response """

    def get_url(self):
        if URLS.get(self.path, False):
            loader = URLS[self.path]()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        
            if type(loader).__name__ != 'main_l':
                self.wfile.write(bytes("<html><head><title>My framework</title></head><body>", "utf-8"))
                self.wfile.write(bytes("{}".format(loader), "utf-8"))
                self.wfile.write(bytes("</body></html>", "utf-8"))
            else:
                self.wfile.write(bytes(loader(), 'utf-8'))


    def do_GET(self):
        self.get_url()
    
    
        

