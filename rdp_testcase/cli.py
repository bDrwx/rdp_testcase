"""Console script for rdp_testcase."""
import sys
import socketserver
import click
from rdp_testcase.testcase2.proxy import ProxyHTTPRequestHandler


@click.command()
def main(args=None):
    """Console script for rdp_testcase."""
    click.echo(
        "Replace this message by putting your code into " "rdp_testcase.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    PORT = 9191
    with socketserver.TCPServer(("", PORT), ProxyHTTPRequestHandler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
