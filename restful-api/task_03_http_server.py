#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Requête reçue : {self.path}")
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            data = {"name": "John", "age": 30, "city": "New York"}
            json_dict = json.dumps(data)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_dict.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

server = HTTPServer(("", 8000), MyHandler)
server.serve_forever()
