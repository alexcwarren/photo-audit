"""Tests for the Photo Audit CLI."""

from typer.testing import CliRunner

from photo_audit.cli import app

runner = CliRunner()


def test_help() -> None:
    """Verify that the application exposes its help documentation."""
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Read-only auditing" in result.output
