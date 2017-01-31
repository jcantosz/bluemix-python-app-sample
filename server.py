''' Starts a simple Python HTTP server to serve static files '''
import os
try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

HTTPD = Server(("", PORT), Handler)
try:
    print "Start serving at port %i" % PORT
    HTTPD.serve_forever()
except KeyboardInterrupt:
    pass
HTTPD.server_close()
