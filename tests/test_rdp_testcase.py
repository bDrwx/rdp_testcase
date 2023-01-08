#!/usr/bin/env python

"""Tests for `rdp_testcase` package."""

import pytest

from click.testing import CliRunner

from rdp_testcase import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--port INTEGER  Port to listen on." in help_result.output
