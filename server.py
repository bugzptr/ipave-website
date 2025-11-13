#!/usr/bin/env python3
"""
Simple HTTP server with correct MIME types for font files
"""
import http.server
import socketserver
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Set correct MIME types for font files
        if self.path.endswith('.woff2'):
            self.send_header('Content-Type', 'font/woff2')
        elif self.path.endswith('.woff'):
            self.send_header('Content-Type', 'font/woff')
        elif self.path.endswith('.ttf'):
            self.send_header('Content-Type', 'font/ttf')
        elif self.path.endswith('.otf'):
            self.send_header('Content-Type', 'font/otf')
        # Add CORS headers for font files
        if any(self.path.endswith(ext) for ext in ['.woff2', '.woff', '.ttf', '.otf']):
            self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

