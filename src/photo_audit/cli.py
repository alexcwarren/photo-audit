"""Command-line interface for Photo Audit."""

import typer

app = typer.Typer(
    name="photo-audit",
    help="Read-only auditing and comparison of photo and video collections.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """Audit local photo and video collections."""
