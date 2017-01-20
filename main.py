#!/usr/bin/env python

from routine import global_routine
from urllib.parse import urlparse,parse_qsl
from http.server import BaseHTTPRequestHandler, HTTPServer
import xmlparser
import index
import message



class HttpServerEntry(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            url = urlparse(self.path)
            query = parse_qsl(url.query)
            query_dict = dict()
            for x, y in query:
                query_dict[x] = y
            result = global_routine.routine("index", **query_dict)
            print("result: {}".format(result))	
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(result, "utf-8"))
        except BaseException as e:
            self.send_response(200)
            self.end_headers()
            print("error",e)
            self.wfile.write(bytes("no such routine", "utf-8"))

    def do_POST(self):
        try:
            url = urlparse(self.path)
            length = int(self.headers['Content-length'])
            data = self.rfile.read(length)
            print("post data:{}".format(data))
            xmlData = xmlparser.parse_xml(data)
            result = global_routine.routine(xmlData.MsgType, **{"data": xmlData})
            print("result: {}".format(result))
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(result, "utf-8"))
        except BaseException as e:
            self.send_response(200)
            self.end_headers()
            print("error", e)
            self.wfile.write(bytes("no such routine", "utf-8"))


def run():
    server_address = ('0.0.0.0', 80)
    httpd = HTTPServer(server_address, HttpServerEntry)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
