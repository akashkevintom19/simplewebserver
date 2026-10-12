from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("Web server is running!")
print("Name: AKASH KEVIN TOM T")
print("Register Number: 26007391")
print("Open http://127.0.0.1:8000 in your browser")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
    server.server_close()
