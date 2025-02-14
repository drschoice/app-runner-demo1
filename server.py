import os
import logging
import http.server
import socketserver

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

PORT = 7777

logger.info("======Loading configuration======")
logger.info('CONFIG')
logger.info(type(os.environ.get('CONFIG')))
logger.info(os.environ.get('CONFIG'))

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()