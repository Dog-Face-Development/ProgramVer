# ProgramVer — Installation

!!! warning "Pre-2.0 layout"
    This page describes the pre-2.0 flat `main.py` layout. As of 2.0.0 the library is the
    `programver` package (`VersionDialog`, `programver/dialog.py`) and `main.py` is a demo,
    not the module itself — see [Known Issues](internal/known-issues.md) for what changed and
    the [README](https://github.com/willtheorangeguy/ProgramVer#readme) for current usage. This
    page is pending a rewrite for 2.0.

## Requirements

| | |
|---|---|
| Python | 3.x with Tkinter |
| Dependencies | None at runtime |

Tkinter is bundled on Windows and macOS; on Linux install `python3-tk` (Debian, Ubuntu) or
`python3-tkinter` (Fedora).

## From source

```bash
git clone https://github.com/willtheorangeguy/ProgramVer
cd ProgramVer
python main.py
```

You will need to supply `imgs/dfdlogo.gif`, `LICENSE.txt`, and `EULA.txt` — see
[Quickstart](./quickstart.md).

Resource paths are resolved against `main.py`'s own location via `get_resource_path`, so the
working directory does not matter.

## As a component in your own project

The intended use. Copy `main.py` into your project and import it:

```python
from main import ProgramVer
ProgramVer()
```

Copy `imgs/` alongside it, or repoint the image paths.

Earlier documentation told you to copy `ProgramVer.py` and `from ProgramVer import *`. There is
no `ProgramVer.py` in this repository — the module is `main.py`, and the function inside it is
`ProgramVer`. Renaming the file to `programver.py` on the way in is reasonable, and then the old
instruction becomes true.

## From PyPI

```bash
pip install programver
programver
```

Two caveats. The console script points at `main:ProgramVer`, which does call `mainloop()`, so it
would work — if the image were present. And the packaging declares `imgs/` as the package root
(`package_dir={"": "imgs"}`, `find_packages(where="imgs")`) where there are no Python packages
at all; only `py_modules=["main"]` ships anything. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Windows executable

Attached to [releases](https://github.com/willtheorangeguy/ProgramVer/releases/latest), built
with PyInstaller. Note that a one-file build unpacks to a temporary directory — `get_resource_path`
resolves against `__file__`, which PyInstaller sets appropriately, so this should hold.

## Verify

```bash
python main.py
```

The window appears with your logo. A `TclError` about `dfdlogo.gif` means the image is still
missing; see [Troubleshooting](./troubleshooting.md).

## Tests

```bash
pip install -r requirements.txt
pytest
```
