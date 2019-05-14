from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8000
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print("Server running at port ", port);
httpd.serve_forever()
