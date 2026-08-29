# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ProgramVer is a Python/tkinter library that displays a customizable `winver`-style version/copyright
dialog — program name, version, copyright notice, and buttons to open a License or EULA file in a
secondary window. It is published to PyPI as `programver`. As of **2.0.0**, it is a real importable
package (`programver.VersionDialog`) rather than a single file meant to be copied into another
project. `main.py` at the repo root is now a runnable demo of the package, not the library itself.

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
xvfb-run -a python -m pytest tests/ --cov=programver --cov-report=term-missing
```

### Lint
```bash
pylint $(git ls-files '*.py')
```

### Run the demo
```bash
python main.py
# or, once installed:
python -m programver
```

## Architecture

The library lives in the `programver/` package:

- `programver/dialog.py` — `VersionDialog`, the public class. Construct it with `app_name`,
  `version`, `copyright_text`, and optional `license_path`, `eula_path`, `license_blurb`,
  `logo_path`, `show_python_powered`, and `window_title`. Call `.show()` to display it.
  If a Tk root already exists, `.show()` opens a `Toplevel` instead of taking over the app with
  its own `mainloop()` — see `_utils.get_or_create_root`.
- `programver/_utils.py` — `get_or_create_root()` (standalone vs. embedded detection) and
  `get_bundled_image_path()` (resolves paths inside `programver/imgs/`, needed for PyPI installs
  where the CWD may differ from the package location).
- `programver/_text_viewer.py` — `TextViewer`, the read-only scrollable `Toplevel` window used to
  display license/EULA text when their buttons are clicked.
- `programver/imgs/` — bundled image assets (currently `pythonpoweredlengthgif.gif`, the
  Python-Powered badge). A consuming project supplies its own logo via `logo_path`.

### Entry points

- `programver/__init__.py` — exposes `VersionDialog` and `__version__`.
- `programver/__main__.py` — `main()`, enabling `python -m programver` (runs a demo dialog).
- `setup.cfg` / `pyproject.toml` / `setup.py` — all register the `programver` console script
  pointing at `programver.__main__:main`.
- `main.py` (repo root) — a second, standalone demo showing how a consuming project would wire up
  `VersionDialog` with its own copyright/license/EULA text. Not imported by the package itself.

### Key files

| Path | Purpose |
|------|---------|
| `programver/dialog.py` | `VersionDialog` — the public API |
| `programver/_utils.py` | Root/Toplevel detection, bundled image path resolution |
| `programver/_text_viewer.py` | `TextViewer` — license/EULA text window |
| `programver/imgs/` | Bundled image assets (Python-Powered badge) |
| `main.py` | Standalone demo entry point |
| `tests/test_main.py` | Unit tests (mocked tkinter) |
| `LICENSE.md` | License text; `main.py`'s demo points its `license_path` here |
| `EULA.md` | EULA text; `main.py`'s demo points its `eula_path` here |
| `pytest.ini` | Pytest configuration (testpaths, addopts) |
| `.deepsource.toml` | DeepSource static analysis config (uses `black` formatter) |

**Customization intent:** `VersionDialog` is now a real, parameterized class — consuming projects
construct it with their own name, version, copyright text, and file paths rather than editing
literals in a copied file. `main.py` demonstrates this usage and is a reasonable starting point to
adapt, but is not itself imported by `programver`.

## Testing

Tests are in `tests/test_main.py` using `unittest.TestCase`:

- `TestVersionDialogInit` — constructor parameter storage and defaults
- `TestVersionDialogShow` — `.show()` behavior: standalone vs. embedded, window title, labels,
  conditional license/EULA buttons, Python-Powered badge, logo
- `TestTextViewer` — the license/EULA viewer window (Toplevel, title, content, read-only state, scrollbar)
- `TestGetOrCreateRoot` — standalone-vs-embedded root detection
- `TestModuleIntegration` — package imports, `VersionDialog` is a class, `__version__` is set,
  the demo `main.py` module imports cleanly

All tkinter calls are mocked with `unittest.mock.patch` so tests run headlessly.

### CI Workflows (`.github/workflows/`)

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `tests.yml` | push/PR to `master` | Runs pytest across Ubuntu/Windows/macOS x Python 3.10-3.12; uploads coverage to Codecov |
| `pylint.yml` | any push | Runs pylint on all `.py` files (Python 3.9) |
| `codeql-analysis.yml` | push/PR to `master`, weekly schedule | CodeQL security scanning |
| `push-to-pypi.yml` | GitHub release published | Builds and publishes to PyPI |

The default branch is `master`.

## Coding Conventions

- 4-space indentation (no tabs).
- Semantic Versioning for releases.
- Version number appears in **four places** — update all on a version bump:
  1. `pyproject.toml` (`[project] version`)
  2. `setup.cfg` (`[metadata] version`)
  3. `setup.py` (`version` kwarg)
  4. `programver/__init__.py` (`__version__`)
- The `# pylint: disable=import-error, invalid-name` comments at the top of `main.py` and
  `test_main.py` are intentional — do not remove them.
- `test_main.py` also disables `wrong-import-position`, `import-outside-toplevel`, and
  `unused-argument` — do not remove these either.
- Black is configured as the code formatter via `.deepsource.toml`.
