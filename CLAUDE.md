# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ProgramVer is a Python/tkinter GUI app that replicates Microsoft's `winver` — it displays a customizable window with program version info, copyright notices, and buttons to open a License or EULA file in a secondary window. It is published to PyPI as `programver` and is designed to be forked and customized per-program. Current version: **1.9.0**.

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
xvfb-run -a python -m pytest tests/test_main.py::TestClassName::test_name -v

# Windows / macOS
python -m pytest tests/test_main.py::TestClassName::test_name -v
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
- `ProgramVer()` — builds and runs the main tkinter window: logo images, version/copyright labels, and two buttons. Calls `window.mainloop()` so it blocks until the window is closed.
- `openLicense()` — opens `LICENSE.txt` in a new `Tk()` window.
- `openEULA()` — opens `EULA.txt` in a new `Tk()` window.

### Entry points

- `__main__.py` — calls `ProgramVer()`, enabling `python -m programver`.
- `__init__.py` — declares `__all__ = ["main"]` for PyPI packaging.
- `setup.cfg` / `pyproject.toml` / `setup.py` — all register the `programver` console script pointing at `main:ProgramVer`.

### Key files

| Path | Purpose |
|------|---------|
| `main.py` | All application logic |
| `tests/test_main.py` | Unit tests (mocked tkinter) |
| `imgs/` | Image assets (`dfdlogo.gif`, `pythonpoweredlengthgif.gif`) |
| `LICENSE.txt` | License text displayed at runtime by `openLicense()` |
| `EULA.txt` | EULA text displayed at runtime by `openEULA()` |
| `pytest.ini` | Pytest configuration (testpaths, addopts) |
| `.deepsource.toml` | DeepSource static analysis config (uses `black` formatter) |

**Customization intent:** The strings inside `ProgramVer()` (window title, version label, trademark text, license blurb) and the image files in `imgs/` are expected to be replaced when the project is forked. `LICENSE.txt` and `EULA.txt` in the repo root are the files opened at runtime.

## Testing

Tests are in `tests/test_main.py` using `unittest.TestCase` with five test classes:

- `TestGetResourcePath` — path resolution helper
- `TestOpenLicense` — license window creation and content display
- `TestOpenEULA` — EULA window creation and content display
- `TestProgramVer` — main window components (images, labels, buttons, commands)
- `TestModuleIntegration` — import and callable checks

All tkinter calls are mocked with `unittest.mock.patch` so tests run headlessly.

### CI Workflows (`.github/workflows/`)

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `tests.yml` | push/PR to `master` | Runs pytest across Ubuntu/Windows/macOS x Python 3.9-3.12; uploads coverage to Codecov |
| `pylint.yml` | any push | Runs pylint on all `.py` files (Python 3.9) |
| `codeql-analysis.yml` | push/PR to `master`, weekly schedule | CodeQL security scanning |
| `push-to-pypi.yml` | GitHub release published | Builds and publishes to PyPI |

The default branch is `master`.

## Coding Conventions

- 4-space indentation (no tabs).
- Semantic Versioning for releases.
- Version number appears in **four places** — update all on a version bump:
  1. `main.py` (the `info` label text)
  2. `pyproject.toml` (`[project] version`)
  3. `setup.cfg` (`[metadata] version`)
  4. `setup.py` (`version` kwarg)
- The `# pylint: disable=import-error, invalid-name` comments at the top of `main.py`, `__main__.py`, `__init__.py`, and `test_main.py` are intentional — do not remove them.
- `test_main.py` also disables `wrong-import-position`, `import-outside-toplevel`, and `unused-argument` — do not remove these either.
- Black is configured as the code formatter via `.deepsource.toml`.
