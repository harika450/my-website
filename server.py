from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Custom handling for specific files
        if self.path == '/text.txt':
            # Send a plain text response
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            with open('text.txt', 'r') as file:
                self.wfile.write(file.read().encode())
        elif self.path == '/audio.mp3':
            # Send an MP3 file
            self.send_response(200)
            self.send_header('Content-type', 'audio/mpeg')
            self.end_headers()
            with open('audio.mp3', 'rb') as file:
                self.wfile.write(file.read())
        else:
            # Default handling for other requests
            super().do_GET()

# Set up and start the server
PORT = 8000
server_address = ('', PORT)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)

print(f"Serving on port {PORT}...")
httpd.serve_forever()
