# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ProgramVer is a Python/tkinter GUI app that replicates Microsoft's `winver` — it displays a customizable window with program version info, copyright notices, and buttons to open a License or EULA file in a secondary window. It is published to PyPI and is designed to be forked and customized per-program.

## Commands

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
# Linux (requires xvfb for headless tkinter)
xvfb-run -a python -m pytest tests/ -v

# Windows / macOS
python -m pytest tests/ -v
```

### Run a single test
```bash
# Linux
xvfb-run -a python -m pytest tests/test_main.py::TestProgramVer::test_name -v

# Windows / macOS
python -m pytest tests/test_main.py::TestProgramVer::test_name -v
```

### Run tests with coverage
```bash
xvfb-run -a python -m pytest tests/ --cov=. --cov-report=term-missing
```

### Lint
```bash
pylint $(git ls-files '*.py')
```

## Architecture

All application logic lives in a single module: **`main.py`**. It exposes four functions:

- `get_resource_path(filename)` — resolves paths relative to the module file (needed for PyPI installs where the CWD may differ from the package location).
- `ProgramVer()` — builds and runs the main tkinter window: logo images, version/copyright labels, and two buttons.
- `openLicense()` — opens `LICENSE.txt` in a new `Tk()` window.
- `openEULA()` — opens `EULA.txt` in a new `Tk()` window.

`__main__.py` is the entry point; it just calls `ProgramVer()`. `setup.cfg` / `pyproject.toml` register the `programver` console script pointing at `main:ProgramVer`.

**Customization intent:** The strings inside `ProgramVer()` (window title, version label, trademark text, license blurb) and the image files in `imgs/` are expected to be replaced when the project is forked. `LICENSE.txt` and `EULA.txt` in the repo root are the files opened at runtime.

## Testing

Tests are in `tests/test_main.py` using `unittest.TestCase`. All tkinter calls are mocked with `unittest.mock.patch` so tests run headlessly. The `# pylint: disable=import-error, invalid-name` comments at the top of both `main.py` and `test_main.py` are intentional — do not remove them.

CI runs the full matrix: Ubuntu, Windows, macOS × Python 3.9–3.12. Coverage target is 100% for `main.py`.

## Coding Conventions

- 4-space indentation (no tabs).
- Semantic Versioning for releases.
- Version number appears in `main.py` (the `info` label), `pyproject.toml`, `setup.cfg`, and `setup.py` — update all four on a version bump.
