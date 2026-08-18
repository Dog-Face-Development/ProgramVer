# ProgramVer — Quickstart

## Before it will run

The repository is missing three files the code opens. Supply them first:

| File | Used by | Notes |
|---|---|---|
| `imgs/dfdlogo.gif` | `ProgramVer()` | Your logo. **GIF or PNG only** — Tkinter reads nothing else |
| `LICENSE.txt` | **Open License** button | Plain text; the repo ships `LICENSE.md` |
| `EULA.txt` | **Open EULA** button | Plain text |

Without the first, the window does not open at all. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Run it

```bash
git clone https://github.com/willtheorangeguy/ProgramVer
cd ProgramVer
python main.py
```

## What you get

A window titled *Copyright & Version Info for ProgramVer*, containing:

- Your logo
- The program name and version
- A trademark notice
- A licence blurb
- **Open License** and **Open EULA** buttons
- The Python-Powered badge

## Use it in your own program

```python
from main import ProgramVer

ProgramVer()   # opens the window and blocks until it is closed
```

`ProgramVer()` calls `mainloop()` itself, so it blocks. Calling it from an existing Tkinter app
means running a second event loop — see [Architecture](./architecture.md).

## Make it yours

Every string in the window is a literal in `main.py` marked `# change as needed`:

| Change | Where |
|---|---|
| Window title | `window.title(...)` in `ProgramVer` |
| Name and version | The `info` label |
| Trademark notice | The `trademarks` label |
| Licence summary | The `licenseblurb` label |
| Licence file | `get_resource_path("LICENSE.txt")` in `openLicense` |
| EULA file | `get_resource_path("EULA.txt")` in `openEULA` |
| Logo | `imgs/dfdlogo.gif` |

The shipped text names a different company and quotes the GPL, while this repository is MIT. It
is placeholder content — replace all of it. See [Configuration](./configuration.md).

## Tests

```bash
pip install -r requirements.txt
pytest
```

14 tests, passing. Read [Testing](./testing.md) before reading anything into that.
