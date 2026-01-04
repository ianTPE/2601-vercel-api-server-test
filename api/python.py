from http.server import BaseHTTPRequestHandler
import json
import sys

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {
            'message': 'Hello from Vercel Python API!',
            'python': sys.version,
            'platform': sys.platform,
            'serializer': 'json'
        }
        
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
