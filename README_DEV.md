# Photo Audit Development

How to develop `photo-audit`.

## Running the application

```powershell
uv run photo-audit --help
```

## Quality checks

```powershell
uv run check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

## Project structure

```plaintext
src/photo_audit/
    __init__.py
    cli.py

tests/
    test_cli.py
```

## Development workflow

1. Create or select a GitHub Issue.
1. Create a feature branch from the latest main.
1. Implement the change and add appropriate tests.
1. Run the project's quality checks.
1. Push and open a pull request.
1. Verify CI before merging.

## Safety principle

> **Media files must never be modified by auditing operations.**
