# ProgramVer — FAQ

## It crashes on startup

`ProgramVer()` loads `imgs/dfdlogo.gif`, which is not in the repository, so Tkinter raises a
`TclError` before the window appears. Supply your own logo at that path — GIF or PNG.

Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

## The License and EULA buttons crash

They read `LICENSE.txt` and `EULA.txt`. Neither exists here — the repository ships `LICENSE.md`,
and there is no EULA. Add plain-text files, or repoint the calls.

## The tests pass, so how is it broken?

The suite mocks every file read and every Tk widget, so it never touches the filesystem or a
display. Every line runs; every line runs against a mock. See [Testing](./testing.md).

## Why does the window show a GPL notice when the repo is MIT?

The blurb, the trademark line, and the version are placeholder content for you to replace — each
marked `# change as needed`. They name a different company and quote the GPL.

For a tool whose purpose is displaying licence information, shipping the wrong licence as the
default is worth fixing. Same known-issues file.

## How do I use it in my program?

```python
from main import ProgramVer
ProgramVer()
```

Copy `main.py` and `imgs/` into your project and edit the strings — see
[Configuration](./configuration.md).

## Earlier docs said to copy `ProgramVer.py`

There is no such file; the module is `main.py`. Renaming it on the way into your project makes
the old instruction true.

## Does it block?

Yes. `ProgramVer()` calls `mainloop()` itself, so it returns when the window is closed. Calling
it from an existing Tkinter app starts a second event loop — see
[Architecture](./architecture.md).

## Can I use a PNG or JPEG logo?

PNG yes, JPEG no. Tkinter's `PhotoImage` reads GIF and PNG only; JPEG needs Pillow.

## Does it need internet, or write anything?

Neither. It reads local files and draws a window.

## Why Tkinter?

Because it is in the standard library. A version window that added a GUI dependency to every
project it was copied into would not be worth copying.

## Is there a Windows executable?

Yes, attached to [releases](https://github.com/willtheorangeguy/ProgramVer/releases/latest).
