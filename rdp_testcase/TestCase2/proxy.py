from http.server import BaseHTTPRequestHandler
from http.client import HTTPConnection
import logging
import re
import socketserver


PORT = 9191


logging.basicConfig(level=logging.DEBUG)
HTTPConnection.debuglevel = 1


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.debug(f"Do get request from client {self.requestline}")
        host = self.headers.get_all("Host")[0]
        conn = HTTPConnection(host)
        conn.request("GET", self.path, headers=self.headers)
        resp = conn.getresponse()
        self.send_response(resp.getcode())
        headers = resp.getheaders()
        for line in headers:
            self.send_header(line[0], line[1])
        contenType = resp.getheader("Content-Type")
        if "text/" in contenType:
            charset = self._get_charset(contenType)
            body = resp.read().decode(charset)
            clear_body = self._clear_from_obscen(body)
            clear_body = clear_body.encode(charset)
            self.send_header("Content-Length", len(clear_body))
            self.end_headers()
            self.wfile.write(clear_body)
        else:
            self.end_headers()
            self.wfile.write(resp.read())
        resp.close()
        conn.close()

    def _clear_from_obscen(self, html: str) -> str:
        return re.sub(
            "(\w*ху[юийеёя]\w*)|(\w*пизд[аыоиеуяю]\w*)|(\w*[её]б[уилаоеы]\w*)|(залуп\w*)",
            "***",
            html,
            flags=re.IGNORECASE,
        )

    def _get_charset(self, content_type: str) -> tuple:
        try:
            charset = re.findall("charset=(\S{3,})$", content_type)[0]
        except (Exception, IndexError):
            charset = "utf-8"
        return charset
