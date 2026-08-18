# ProgramVer — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/ProgramVer
cd ProgramVer
pip install -r requirements.txt
python main.py
```

No runtime dependencies; `requirements.txt` is the tooling.

## Commands

```bash
python main.py                     # run
pytest                             # 14 tests
pylint $(git ls-files '*.py')      # what CI lints with
```

## Packaging

`pyproject.toml`, `setup.py`, and `setup.cfg` all describe the package at version `1.9.0`. Two of
them contain a mistake worth understanding before touching them:

```python
packages=find_packages(where="imgs"),
package_dir={"": "imgs"},
py_modules=["main"],
```

`imgs/` holds images, not Python packages, so `find_packages` finds nothing and the `package_dir`
mapping points the root at a directory with no modules in it. Only `py_modules=["main"]` actually
ships code. `setup.cfg` repeats the same mapping.

`MANIFEST.in` lists `imgs/dfdlogo.gif` and `imgs/pythonpoweredlengthgif.gif`. The first is not in
the repository. See [`internal/known-issues.md`](./internal/known-issues.md).

Consolidating on `pyproject.toml` would remove the duplication and the chance of the three
drifting.

## Style

- **Pylint**, with per-file disables at the top (`import-error`, `invalid-name`).
- **Module docstring and copyright header** on every file.
- **`get_resource_path` for every file access.** Never a bare relative path — it is what makes the
  module portable into another project.
- **GIF or PNG images.** Tkinter reads nothing else without Pillow, and Pillow would be the first
  runtime dependency.

## If you change the display strings

They are the template's whole surface, and [Configuration](./configuration.md) names each by
symbol. The old `CUSTOMIZATION.md` located them by **line number**, which had drifted out of
date — avoid reintroducing that.

## If you extend the tests

Mock the display, not the filesystem. See [Testing](./testing.md) — the current suite mocks both,
which is why it passes against missing files.

## CI

| Workflow | Does |
|---|---|
| `tests.yml` | pytest |
| `pylint.yml` | Lint |
| `codeql-analysis.yml` | Security scan |
| `push-to-pypi.yml` | Publish on release |

Nothing runs the built package, so a release that cannot start still publishes green.

## Recording defects

Bugs found while working here go in [`internal/known-issues.md`](./internal/known-issues.md)
rather than being fixed in passing, unless fixing them is the job you are on.
