# ProgramVer — Troubleshooting

## `TclError: couldn't open ".../imgs/dfdlogo.gif"`

The file is not in the repository, and the code needs it before the window can appear. Supply
your own logo at `imgs/dfdlogo.gif` — GIF or PNG.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md). `MANIFEST.in` lists it, so
it is expected to exist.

## `FileNotFoundError: LICENSE.txt` / `EULA.txt`

The **Open License** and **Open EULA** buttons read those exact filenames. Neither is in the
repository. Add them as plain text, or edit `openLicense` and `openEULA` to point at files you
have — the repository's own licence is `LICENSE.md`.

## `TclError: couldn't recognize data in image file`

The image is not a GIF or PNG. Tkinter reads nothing else without Pillow.

## A label is blank where an image should be

Tkinter keeps no Python reference to a `PhotoImage`. In the current code they survive because
`ProgramVer()` blocks in `mainloop()` and they stay in scope. If you refactor it to return the
window, bind each image to a widget attribute (`label.image = img`) or they will vanish silently.

## `ModuleNotFoundError: No module named 'tkinter'`

A separate package on most Linux distributions:

```bash
sudo apt install python3-tk        # Debian, Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

## Closing the License window closed everything

`openLicense` and `openEULA` each construct a second `Tk()` root rather than a `Toplevel()`.
Multiple roots share one interpreter, so destroying the wrong one can take the others down. See
[Architecture](./architecture.md).

## The version or copyright is wrong

They are placeholder literals in `main.py` — the shipped text names a different company and a
2024 date. [Configuration](./configuration.md) names each by symbol.

## `pip install programver` then `programver` fails

The console script itself is wired correctly (`main:ProgramVer`, which does call `mainloop()`),
but it fails on the missing image like any other route. The packaging also declares `imgs/` as
the package root, which is wrong but harmless — only `py_modules=["main"]` ships code. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Old docs referenced line numbers that do not match

`docs/CUSTOMIZATION.md` located each editable string by line number, and the file has changed
since. [Configuration](./configuration.md) names symbols instead.

## Tests pass but the program does not run

Expected, and the point of the [Testing](./testing.md) page: the suite mocks the filesystem as
well as the display.

## Still stuck

[Open an issue](https://github.com/willtheorangeguy/ProgramVer/issues/new/choose) or ask on the
[Discord](https://discord.gg/x3G8adwVUe), with your OS, Python version, and the traceback.
