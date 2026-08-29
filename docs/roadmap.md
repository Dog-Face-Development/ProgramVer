# ProgramVer — Roadmap

!!! warning "Pre-2.0 layout"
    This page describes the pre-2.0 flat `main.py` layout. As of 2.0.0 the library is the
    `programver` package (`VersionDialog`, `programver/dialog.py`) and `main.py` is a demo,
    not the module itself — see [Known Issues](internal/known-issues.md) for what changed and
    the [README](https://github.com/willtheorangeguy/ProgramVer#readme) for current usage. This
    page is pending a rewrite for 2.0.

Direction, not a schedule. Defects are in
[`internal/known-issues.md`](./internal/known-issues.md).

## Where it is

A working template that does not currently run, because three files it opens are absent.
Everything else — the layout, the customisation points, the resource resolution — is sound.

## Considered

**Restoring the missing files.** `imgs/dfdlogo.gif`, `LICENSE.txt`, and `EULA.txt`. The first
alone is the difference between a program that starts and one that does not.

**A test that the resources exist.** Four lines, no mocking, and it would have caught all three.

**Defaults that match this repository.** The window shows a GPL notice and another company's
copyright while the repo is MIT — placeholder text that a tool for displaying licences should
not ship.

**Reading the version from package metadata** rather than a hardcoded string, so a release bump
reaches the window.

**Fixing the packaging.** `package_dir={"": "imgs"}` and `find_packages(where="imgs")` point at a
directory with no packages.

**`Toplevel()` for the licence and EULA windows** instead of second `Tk()` roots.

**Graceful degradation.** A missing logo could render a placeholder and a missing licence file an
explanatory message, rather than a traceback — for a template others will copy half-configured,
that is friendlier than failing hard.

## Non-goals

**A configuration file.** Editing the literals is the workflow; a schema for values a developer
sets once would be more machinery than the component.

**A GUI toolkit dependency.** Tkinter is in the standard library, and staying there is what makes
this safe to copy into any project.

**Rich text or Markdown rendering.** The licence is displayed as plain text in a `Text` widget.
Rendering would mean a dependency, for a document nobody reads carefully in a dialog.

**Becoming a general About-box framework.** It shows version and licence information. Update
checks, credits screens, and telemetry consent are all different things.

## Contributing

Issues and pull requests welcome — see the
[Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) or
the [Discord](https://discord.gg/x3G8adwVUe).

Adding `imgs/dfdlogo.gif` is the smallest change that turns this back into a working program.
