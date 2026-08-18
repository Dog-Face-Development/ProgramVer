# ProgramVer — Architecture

One module, three functions, no dependencies.

```
main.py
├── get_resource_path(filename)   resolve against __file__
├── openLicense()                 read LICENSE.txt → its own window
├── openEULA()                    read EULA.txt    → its own window
└── ProgramVer()                  the main window, then mainloop()
```

## `get_resource_path`

```python
base_dir = os.path.dirname(os.path.abspath(__file__))
return os.path.join(base_dir, filename)
```

Resolves against the **module**, not the working directory, so the window works wherever it is
launched from and survives being copied into another project. Used for both images and both text
files.

## `ProgramVer()`

Builds the window and calls `mainloop()` itself, so it **blocks** until closed. That makes it a
drop-in call from a menu handler, and it means calling it from an existing Tkinter application
starts a second event loop — see below.

Widgets, top to bottom: logo, name and version, trademark notice, licence blurb, the two
buttons, and the Python-Powered badge at the bottom.

Note that neither `PhotoImage` is bound to a lasting reference. They survive because they are
locals of a function that blocks in `mainloop()` — if `ProgramVer()` were refactored to return
the window instead, both images would be garbage-collected and the labels would render blank
with no error.

## `openLicense` and `openEULA`

Identical in shape: construct a `Tk()`, read a text file, insert it into a `Text` widget, pack.

Two things follow. Neither calls `mainloop()` — they rely on the main window's loop, which works
because they are invoked from a button callback inside it. And both construct a second `Tk()`
root rather than a `Toplevel()`; Tkinter supports one true root per process, so closing the
wrong window can take the others with it.

Neither file is present in the repository. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Why it is a template, not a library

Every displayed string is a literal, each marked `# change as needed`. There is no parameter, no
config object, and no settings file. The intended workflow is copying `main.py` into your project
and editing it.

That is a reasonable design for a component this small — a configurable version would need a
schema for something a developer edits once — but it does mean the shipped defaults are visible
to anyone who forgets to change them.

## Standard library only

Tkinter and `os`. Nothing to install, and nothing added to the dependency tree of whatever
project copies it in.

## What breaks it

The design is sound; three files it opens are absent. `imgs/dfdlogo.gif` stops the window
entirely, and the two `.txt` files break a button each. `MANIFEST.in` lists the image for
packaging, so its absence is an omission rather than a decision.
