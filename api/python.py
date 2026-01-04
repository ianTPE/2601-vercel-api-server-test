from http.server import BaseHTTPRequestHandler
import orjson
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
            'serializer': 'orjson'
        }
        
        # orjson.dumps returns bytes, so no need to encode('utf-8')
        self.wfile.write(orjson.dumps(data))
        return
