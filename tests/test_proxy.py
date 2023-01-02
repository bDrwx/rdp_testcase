from io import BytesIO as IO
import pytest
from rdp_testcase.testcase2.proxy import ProxyHTTPRequestHandler


@pytest.fixture(scope="module")
def get_handler():
    """Test the custom HTTP request handler by mocking a server"""

    class MockRequest(object):
        def makefile(self, *args, **kwargs):
            return IO(b"GET /index.html HTTP/1.1\r\nHost: localhost:8080\r\n\r\n")

        def sendall():
            pass

    class MockServer(object):
        def __init__(self, ip_port, Handler):
            handler = Handler(MockRequest(), ip_port, self)

    # The GET request will be sent here
    # and any exceptions will be propagated through.
    server = MockServer(("0.0.0.0", 8888), ProxyHTTPRequestHandler)
    return server


def test_obscen_cliar(get_handler):
    pass
