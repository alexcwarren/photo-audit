# Photo Audit

A read-only Python CLI for auditing, cataloging, and comparing
large photo and video collections.

Photo Audit aims to help identify exact duplicates, compare
collections across different storage devices, and discover
files that may exist in only one location.

## Project Status

**Early development (pre-v0.1.0)**

The CLI foundation is established. Media scanning and
auditing functionality are under development.

## Safety

Photo Audit is designed around a read-only approach.

The tool will not delete, rename, move, overwrite, or
modify the original media files being audited.

Scan results will be stored separately in a SQLite database.

## Planned Features

The initial release aims to provide:

- Recursive discovery of photos and videos.
- Filesystem and image metadata extraction.
- Cryptographic file hashing.
- Persistent SQLite storage.
- Named collection sources.
- Collection summaries.
- Exact duplicate detection.
- Comparison of different sources.
- Identification of files unique to a particular source.

Future releases may introduce similar-photo detection,
incremental scanning, HTML reports, and archive validation.

## Development Installation

Requirements:

- Python 3.12 or newer, subject to project configuration.
- uv

Clone the repository and install the development environment:

```powershell
uv sync
```

Verify the CLI:

```powershell
uv run photo-audit --help
```

See [README_DEV.md](README_DEV.md) for development instructions.
