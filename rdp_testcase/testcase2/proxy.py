import logging
import re
import sys
from http.server import BaseHTTPRequestHandler

import requests

logging.basicConfig(level=logging.DEBUG)


class ProxyHTTPRequestHandler(BaseHTTPRequestHandler):
    """Реализация обработчика HTTP запросов позволяющего фильтровать нецензурную лексику
    в html страницах получаемых с WEB сервера по протоколу HTTP

    Args:
        BaseHTTPRequestHandler (_type_): _description_
    """

    def do_GET(self):
        """Метод обрабатывающий GET запросы"""
        logging.debug("Do get request from client %s", self.requestline)
        self._handle_request(self.path, self.headers)

    def _clear_from_obscen(self, html: str) -> str:
        return re.sub(
            r"(\w*ху[юийеёя]\w*)|(\w*пизд[аыоиеуяю]\w*)|(\w*[её]б[уилаоеы]\w*)|(залуп\w*)",
            r"***",
            html,
            flags=re.IGNORECASE,
        )

    def _get_charset(self, content_type: str) -> str:
        try:
            charset = re.findall(r"charset=(\S{3,})$", content_type)[0]
        except IndexError:
            charset = "UTF-8"
        return charset

    def _handle_request(self, url, headers):
        try:
            resp = requests.get(url, headers=headers, stream=True, timeout=10)
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
            logging.debug("Exception %s occurs while handling %s", e, url)
            self.send_error(504, str(e))
