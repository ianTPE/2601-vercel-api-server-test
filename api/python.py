from http.server import BaseHTTPRequestHandler
import json
import sys
import sys
from datetime import datetime, timezone, timedelta

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

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            body = json.loads(post_data.decode('utf-8'))
            
            response = {
                'received': body,
                'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds') 
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error_response = {
                'error': 'Invalid JSON body',
                'details': str(e)
            }
            self.wfile.write(json.dumps(error_response).encode('utf-8'))
