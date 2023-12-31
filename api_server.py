#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import http.server
import socketserver

class api_server(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Pong')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not Found')

PORT = 8080

with socketserver.TCPServer(("", PORT), api_server) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()


# In[ ]:




