# ProgramVer — Configuration

!!! warning "Pre-2.0 layout"
    This page describes the pre-2.0 flat `main.py` layout. As of 2.0.0 the library is the
    `programver` package (`VersionDialog`, `programver/dialog.py`) and `main.py` is a demo,
    not the module itself — see [Known Issues](internal/known-issues.md) for what changed and
    the [README](https://github.com/willtheorangeguy/ProgramVer#readme) for current usage. This
    page is pending a rewrite for 2.0.

ProgramVer is a template. There is no config file — you edit `main.py`, and every editable
string carries a `# change as needed` comment.

Earlier documentation gave **line numbers** for these edits. They no longer match the file, so
this page names the symbols instead.

## The window title

```python
window.title("Copyright & Version Info for ProgramVer")
```

In `ProgramVer()`. Use your program's name.

## Program name and version

```python
info = Label(window, text="ProgramVer \n Version: 1.9.0 (Build #)")
```

Hardcoded. Reading it from your package metadata
(`importlib.metadata.version("yourpackage")`) keeps it from drifting after a release.

## Trademark notice

```python
trademarks = Label(window, text="Copyright (C) 2017 - 2024 Dog Face Development Co. ...")
```

Placeholder text naming a different company, and dated 2024. Replace it. The `winver` equivalent
is a single line:

```text
© Microsoft Corporation. All rights reserved.
```

## Licence blurb

```python
licenseblurb = Label(window, text="""...GNU General Public License...""")
```

The shipped text is the GPL v3 notice for "Dog Face Development Company", while **this repository
is MIT**. For a tool whose purpose is displaying licence information, showing the wrong licence
is worth fixing before anything else — see
[`internal/known-issues.md`](./internal/known-issues.md).

Use the notice your own licence recommends. MIT does not require one in-window; GPL does.

## The licence and EULA files

```python
license_path = get_resource_path("LICENSE.txt")   # in openLicense
eula_path    = get_resource_path("EULA.txt")      # in openEULA
```

Both are read as plain text with UTF-8 encoding and shown in a `Text` widget. Neither file is in
this repository — supply them, or repoint the calls at files you have.

If you point `openLicense` at a Markdown file, note it is displayed raw, with no rendering.

## Images

| Image | Path | Shown |
|---|---|---|
| Your logo | `imgs/dfdlogo.gif` | Top |
| Python-Powered badge | `imgs/pythonpoweredlengthgif.gif` | Bottom |

**GIF or PNG only** — Tkinter's `PhotoImage` reads nothing else without Pillow. Both are loaded
through `get_resource_path`, so they resolve relative to the module.

Remember `MANIFEST.in` if you add images and intend to package them.

## Layout

Everything is `pack`ed: logo, info, trademarks, blurb, and buttons from the top; the Python badge
at the bottom. Buttons get `pady=5`. There is no styling beyond Tkinter's defaults, deliberately —
it is meant to look like a system dialog.
