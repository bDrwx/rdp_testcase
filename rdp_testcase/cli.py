"""Console script for rdp_testcase."""
import socketserver
import sys

import click

from rdp_testcase.testcase2.proxy import ProxyHTTPRequestHandler


@click.command()
@click.option("--port", default=8000, help="Port to listen on.")
def main(port):
    """Console script for rdp_testcase."""
    click.echo(f"Obscen free http proxy for RDP.RU. Server listening on port {port}")
    with socketserver.TCPServer(("", port), ProxyHTTPRequestHandler) as httpd:
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
