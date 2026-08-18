# ProgramVer — Testing

```bash
pip install -r requirements.txt
pytest
```

14 tests, passing, in about a tenth of a second.

## What is covered

`tests/test_main.py` exercises all four functions:

| Test group | Asserts |
|---|---|
| `get_resource_path` | The returned path ends with the requested filename |
| `openLicense` | A window is created and a file is opened |
| `openEULA` | The same, for the EULA |
| `ProgramVer` | The widgets are constructed and packed |

`unittest.mock` supplies `mock_open` for file reads and patches `main.Tk`, `main.Text`,
`main.Label`, `main.Button`, and `main.PhotoImage`.

## What is not covered, and it matters here

Mocking every file read and every widget is what lets the suite run headless in CI. It also means
the suite passes on a program that cannot start.

Concretely: `test_get_resource_path` asserts the returned string **ends with** `dfdlogo.gif`. It
never checks that the file exists — and it does not. `test_openLicense_creates_window` patches
`builtins.open` with `mock_open`, so `LICENSE.txt` being absent is invisible.

So "100% coverage of the main module", as earlier documentation put it, is true and says nothing
about whether the program works. Every line executes; every line executes against a mock.

## Worth adding

A test that the files the code opens are actually in the repository:

```python
def test_required_resources_exist(self):
    for name in ("imgs/dfdlogo.gif", "imgs/pythonpoweredlengthgif.gif",
                 "LICENSE.txt", "EULA.txt"):
        self.assertTrue(os.path.exists(get_resource_path(name)), name)
```

Four lines, no mocking, and it would have caught all three of this repository's High-severity
issues. Recorded in [`internal/known-issues.md`](./internal/known-issues.md).

The general point is worth keeping in mind when extending the suite: mock the **display**, not
the **filesystem**. The display cannot be exercised in CI; the filesystem can.

## CI

`.github/workflows/tests.yml` runs the suite on push and pull request. `pylint.yml` lints,
`codeql-analysis.yml` scans, `push-to-pypi.yml` publishes on release.
