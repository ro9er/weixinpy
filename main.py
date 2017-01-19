#!/usr/bin/env python

from routine import global_routine
from index import *
from urllib.parse import urlparse,parse_qsl
from http.server import BaseHTTPRequestHandler, HTTPServer



class HttpServerEntry(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            url = urlparse(self.path)
            query = parse_qsl(url.query)
            query_dict = dict()
            for x, y in query:
                query_dict[x] = y
            result = global_routine.routine(url.path, **query_dict)
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
