# Known Issues — ProgramVer

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.


**6 open:** 2 high, 3 medium, 1 low.

## 1. The window cannot open: imgs/dfdlogo.gif is not in the repository

**Severity:** High  
**Where:** `main.py` -> `ProgramVer`, `MANIFEST.in`

**What:** `ProgramVer()` calls `PhotoImage(file=get_resource_path("imgs/dfdlogo.gif"))` as the first of its two images. `imgs/` contains only `pythonpoweredlengthgif.gif` and an egg-info directory -- `dfdlogo.gif` is absent, and `git ls-files` does not list it. `MANIFEST.in` explicitly includes it for packaging, so its absence is an omission rather than a decision.

**Why it matters:** Tkinter raises `TclError` on that line, before any widget is packed, so the program produces a traceback and no window at all. This is the only thing the package does: there is no degraded mode, no fallback image, and no other entry point. Every route -- `python main.py`, the `programver` console script, the PyInstaller build, and copying the module into another project -- fails identically. CI stays green throughout, because the test suite patches `main.PhotoImage`.

**Suggested fix:** Restore or replace `imgs/dfdlogo.gif` (GIF or PNG; Tkinter reads nothing else without Pillow). Consider falling back to a text label when the image is missing, since this is a template others copy half-configured.

## 2. Both document buttons read files that do not exist

**Severity:** High  
**Where:** `main.py` -> `openLicense`, `openEULA`

**What:** `openLicense` opens `get_resource_path("LICENSE.txt")` and `openEULA` opens `get_resource_path("EULA.txt")`, each with a bare `open(...)` and no guard. Neither file is in the repository: the licence here is `LICENSE.md`, and there is no EULA at all.

**Why it matters:** The two buttons are half the window's function -- a version dialog whose entire value is making the licence one click away. Both raise `FileNotFoundError` from inside a Tk callback, which prints a traceback to the console and leaves the window looking unresponsive rather than reporting anything to the user. A `.md` file sitting next to a `.txt` reference is exactly the kind of near-miss that survives review.

**Suggested fix:** Add plain-text `LICENSE.txt` and `EULA.txt`, or point the calls at files that exist. Either way, wrap the read and show the error in the window instead of the console -- a template will be copied into projects where these filenames are wrong.

## 3. The test suite mocks the filesystem, so it passes against a program that cannot start

**Severity:** Medium  
**Where:** `tests/test_main.py`

**What:** All 14 tests patch `main.Tk`, `main.Text`, `main.Label`, `main.Button`, `main.PhotoImage`, and `builtins.open` (via `mock_open`). `test_get_resource_path` asserts only that the returned string **ends with** `dfdlogo.gif` -- never that the path resolves. Earlier documentation reported '100% code coverage for the main module'.

**Why it matters:** Both High-severity issues above are missing files, and both are invisible to this suite by construction. The result is a repository whose badge, coverage figure, and CI all report health while the program raises before drawing a window. Mocking the display is necessary for headless CI; mocking the filesystem as well removes the only check that would have caught this, and the coverage number then actively misleads.

**Suggested fix:** Add a test that the resources exist -- roughly four lines, no mocking:

    for name in ("imgs/dfdlogo.gif", "imgs/pythonpoweredlengthgif.gif",
                 "LICENSE.txt", "EULA.txt"):
        assert os.path.exists(get_resource_path(name)), name

Keep mocking Tk; stop mocking `open` in tests whose purpose is to prove a file is read.

## 4. The window displays a GPL notice and another company's copyright, in an MIT repository

**Severity:** Medium  
**Where:** `main.py` -> `trademarks`, `licenseblurb`, `info` labels; `LICENSE.md`

**What:** The `trademarks` label reads 'Copyright (C) 2017 - 2024 Dog Face Development Co. All rights reserved in all countries', and `licenseblurb` renders the GNU GPL v3 notice for 'Dog Face Development Company'. `LICENSE.md` in this repository is **MIT, Copyright 2026 willtheorangeguy**. Each label carries a `# change as needed` comment, so the text is placeholder by design.

**Why it matters:** The program's single purpose is displaying accurate copyright and licence information, and its default output is neither -- wrong licence, wrong holder, wrong year. Anyone who copies the template and forgets one label ships a false licence claim in their own About box, which is the specific failure this tool exists to prevent. The `# change as needed` comments make the intent clear in the source and are invisible in the running window.

**Suggested fix:** Make the defaults match this repository -- MIT, willtheorangeguy, the current year -- so an unedited copy is at least self-consistent. Better still, derive the name and version from package metadata and read the notice from the licence file, leaving less to be forgotten.

## 5. Packaging declares imgs/ as the package root, where there are no packages

**Severity:** Medium  
**Where:** `setup.py`, `setup.cfg`

**What:** `setup.py` has `packages=find_packages(where="imgs")` and `package_dir={"": "imgs"}`; `setup.cfg` repeats `package_dir = \n    = imgs` with `packages = find:` under `where = imgs`. `imgs/` contains image files and an egg-info directory -- no Python packages. `find_packages` therefore returns an empty list, and only `py_modules=["main"]` ships any code. A third description of the same package exists in `pyproject.toml`.

**Why it matters:** The build succeeds and publishes, which is why this has survived: the wheel happens to contain the one module that matters, by a different mechanism than the one the configuration appears to be using. Anyone adding a real package later will find it silently excluded, and the `package_dir` mapping makes the failure hard to read -- setuptools will look for modules under `imgs/`. Three overlapping build descriptions make it likelier that a fix lands in the file that is not being read.

**Suggested fix:** Drop the `package_dir` and `find_packages` lines -- this is a single-module project and `py_modules` is the correct declaration. Then consolidate on `pyproject.toml` and delete `setup.py` and `setup.cfg`.

## 6. The README's integration instructions name a file that does not exist

**Severity:** Low  
**Where:** `README.md` (corrected in this pass), `docs/CUSTOMIZATION.md` (removed in this pass)

**What:** The How To Use section instructed: 'Copy the `ProgramVer.py` file to your project's main directory', then 'add `from ProgramVer import *`' and 'call ProgramVer through the `ProgramVer()` function'. There is no `ProgramVer.py` -- the module is `main.py`. Separately, `docs/CUSTOMIZATION.md` located each editable string by line number ('_Line 11_', '_Line 40_'), and those no longer match `main.py`.

**Why it matters:** Copying the module into another project is the documented primary use, and the instructions for it name the wrong file -- so a reader either copies nothing or copies `main.py` and finds the import line wrong too. The line-number references fail more quietly: they point at real lines containing different code, so someone following them edits the wrong string and gets a window that still shows the old text.

**Suggested fix:** Fixed in this pass -- the README and `docs/configuration.md` now name `main.py` and locate each editable string by symbol rather than line number. Renaming the module to `programver.py` would make the original instructions true and is worth considering, since `main.py` is a poor name for a file meant to be dropped into someone else's project.


---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
