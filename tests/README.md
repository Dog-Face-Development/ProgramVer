# ProgramVer Test Suite

This directory contains the comprehensive test suite for ProgramVer.

## Running Tests

### Prerequisites

Install the required testing dependencies:

```bash
pip install -r requirements.txt
```

On Linux systems, you'll also need to install tkinter and xvfb for headless GUI testing:

```bash
sudo apt-get install python3-tk xvfb
```

### Running All Tests

To run all tests:

```bash
# On Linux (headless environment)
xvfb-run -a python -m pytest tests/ -v

# On Windows/macOS (with display)
python -m pytest tests/ -v
```

### Running Tests with Coverage

To run tests with coverage report:

```bash
# On Linux
xvfb-run -a python -m pytest tests/ --cov=. --cov-report=term-missing --cov-report=html

# On Windows/macOS
python -m pytest tests/ --cov=. --cov-report=term-missing --cov-report=html
```

The HTML coverage report will be generated in the `htmlcov` directory.

### Running Specific Tests

To run a specific test file:

```bash
xvfb-run -a python -m pytest tests/test_main.py -v
```

To run a specific test class:

```bash
xvfb-run -a python -m pytest tests/test_main.py::TestOpenLicense -v
```

To run a specific test method:

```bash
xvfb-run -a python -m pytest tests/test_main.py::TestOpenLicense::test_openLicense_creates_window -v
```

## Test Structure

The test suite is organized as follows:

- `test_main.py` - Tests for the main ProgramVer module
  - `TestOpenLicense` - Tests for the openLicense function
  - `TestOpenEULA` - Tests for the openEULA function
  - `TestProgramVer` - Tests for the ProgramVer main function
  - `TestModuleIntegration` - Integration tests for the module

## GitHub Actions Integration

The test suite is automatically run on GitHub Actions for every push and pull request. The workflow:

- Runs on Ubuntu, Windows, and macOS
- Tests against Python 3.9, 3.10, 3.11, and 3.12
- Generates coverage reports
- Uploads coverage to Codecov (for master branch)

See `.github/workflows/tests.yml` for the complete configuration.

## Writing New Tests

When adding new features to ProgramVer, please add corresponding tests following these guidelines:

1. Create test classes that inherit from `unittest.TestCase`
2. Use descriptive test method names that start with `test_`
3. Use mocking for GUI components to avoid requiring a display
4. Add docstrings to explain what each test verifies
5. Ensure tests are independent and can run in any order

## Coverage Goals

We aim to maintain at least 90% code coverage for the main module. Currently, we have 100% coverage for `main.py`.
