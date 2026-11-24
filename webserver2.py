
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

# Set the folder containing index.html
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create the web server
server_address = ("", 8000)
http_server = HTTPServer(
    server_address,
    SimpleHTTPRequestHandler
)

print("Web server started successfully!")
print("Open http://localhost:8000 in your browser.")
print("Press Ctrl+C to stop the server.")

try:
    http_server.serve_forever()
except KeyboardInterrupt:
    print("\nWeb server stopped.")
    http_server.server_close()
