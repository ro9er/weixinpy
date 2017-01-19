#!/usr/bin/env python

import routine
from http.server import BaseHTTPRequestHandler, HTTPServer


@routine.routine('/')
def index(request = None, response = None):
    print("haha")
    return "haha"


class HttpServerEntry(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            result = routine.global_routine.routine(self.path)
            self.send_response(200)
            self.wfile.write(bytes(result, "utf-8"))
        except ValueError as ve:
            self.send_error(404)
            self.wfile.write(bytes("no such routine", "utf-8"))

    def do_POST(self):
        pass


def run():
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, HttpServerEntry)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
