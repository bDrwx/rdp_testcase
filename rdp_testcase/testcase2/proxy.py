import logging
import re
import sys
from http.server import BaseHTTPRequestHandler

import requests

logging.basicConfig(level=logging.DEBUG)


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.debug(f"Do get request from client {self.requestline}")
        self._handle_request(self.path, self.headers)

    def _clear_from_obscen(self, html: str) -> str:
        return re.sub(
            "(\w*ху[юийеёя]\w*)|(\w*пизд[аыоиеуяю]\w*)|(\w*[её]б[уилаоеы]\w*)|(залуп\w*)",
            "***",
            html,
            flags=re.IGNORECASE,
        )

    def _get_charset(self, content_type: str) -> str:
        try:
            charset = re.findall("charset=(\S{3,})$", content_type)[0]
        except (Exception, IndexError):
            charset = "UTF-8"
        return charset

    def _handle_request(self, url, headers):
        try:
            resp = requests.get(url, headers=headers, stream=True)
            if "text/html" in resp.headers["content-type"] and resp.status_code == 200:
                charset = self._get_charset(resp.headers["content-type"])
                resp.encoding = charset
                body = self._clear_from_obscen(resp.text)
                body = body.encode(resp.encoding)
                resp.headers["Content-Length"] = len(body)
            self.send_response(resp.status_code)
            for key in resp.headers:
                self.send_header(key, resp.headers[key])
            self.end_headers()
            self.wfile.write(body if body else resp.content)
        except (requests.ConnectionError, requests.ConnectTimeout):
            e = sys.exc_info()[1]
            logging.debug(f"Exception {e} occurs while handling {url}")
            self.send_error(504, str(e))
