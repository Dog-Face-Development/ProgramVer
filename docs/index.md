# ProgramVer — Documentation

A `winver`-style copyright and version window for your own Python programs: a logo, a version
line, a trademark notice, a licence blurb, and buttons that open the full licence and EULA.

```text
ProgramVer/
├── main.py          get_resource_path, openLicense, openEULA, ProgramVer
├── imgs/            the window's images
├── tests/test_main.py
└── docs/            this documentation
```

## Pages

- [Quickstart](./quickstart.md) — run it, and what you must supply first
- [Installation](./installation.md) — source, PyPI, executable
- [Configuration](./configuration.md) — every string and image to change for your project
- [Architecture](./architecture.md) — three functions, one window
- [Development](./development.md) — packaging and style
- [Testing](./testing.md) — the suite, and what it does not check
- [FAQ](./faq.md) — why it fails, what to customise, why GPL text
- [Troubleshooting](./troubleshooting.md) — missing files, blank windows
- [Roadmap](./roadmap.md) — direction and non-goals
- [Known issues](./internal/known-issues.md) — recorded defects

## It does not run as shipped

Three files the code needs are absent from the repository:

| Wanted by | File | Present |
|---|---|---|
| `ProgramVer()` | `imgs/dfdlogo.gif` | **No** |
| `openLicense()` | `LICENSE.txt` | **No** — the repo has `LICENSE.md` |
| `openEULA()` | `EULA.txt` | **No** |

The first stops the window opening at all. `MANIFEST.in` lists `imgs/dfdlogo.gif` for packaging,
so it is expected to exist and does not.

CI is green throughout, because the test suite mocks file access and every Tk widget. See
[`internal/known-issues.md`](./internal/known-issues.md).

## What it is for

Microsoft's `winver` shows a small window with the product name, version, and licensing notice.
ProgramVer is the same idea for a Python program: a function you call from an About menu that
presents the same information, with the licence text one click away.

The design assumption is that **you edit it**. Program name, version, trademark line, licence
blurb, and the two document filenames are all literals in `main.py`, each with a
`# change as needed` comment. That is the intended workflow — see
[Configuration](./configuration.md).

## Standard library only

Tkinter and nothing else. Dropping `main.py` into a project adds no dependencies, which is the
point of a component meant to be copied rather than depended on.
