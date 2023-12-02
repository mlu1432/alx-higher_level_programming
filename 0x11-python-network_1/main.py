from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open('templates/index.html', 'r') as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, 'utf8'))

        except FileNotFoundError:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404: File not found')

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 5000...")
    httpd.serve_forever()
