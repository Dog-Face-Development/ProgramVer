<!-- Logo -->
<h1 align="center">
  <img src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/ProgramVer/logo.png" height="250px" width="400px" alt="ProgramVer">
  <br>
  ProgramVer
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A Python version of Microsoft's <code>winver</code> — a copyright and licence window you drop into your own program.</h4>

<!-- Badges -->
<div align="center">
  <img alt="PyPI Build State" src="https://github.com/willtheorangeguy/ProgramVer/actions/workflows/push-to-pypi.yml/badge.svg">
  <img alt="Pylint State" src="https://github.com/willtheorangeguy/ProgramVer/actions/workflows/pylint.yml/badge.svg">
  <img alt="Tests State" src="https://github.com/willtheorangeguy/ProgramVer/actions/workflows/tests.yml/badge.svg">
  <img alt="CodeQL State" src="https://github.com/willtheorangeguy/ProgramVer/actions/workflows/codeql-analysis.yml/badge.svg">
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/willtheorangeguy/ProgramVer?include_prereleases">
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/willtheorangeguy/ProgramVer">
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/willtheorangeguy/ProgramVer">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#status">Status</a> •
  <a href="#key-features">Key Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<!-- Screenshot -->
<div align="center">
    <img alt="ProgramVer window" src="https://raw.githubusercontent.com/willtheorangeguy/.github/main/icons/ProgramVer/welcome.png">
</div>

## Status

**Currently broken as shipped.** `ProgramVer()` loads `imgs/dfdlogo.gif`, which is not in the repository, so the window fails before it appears. The two buttons read `LICENSE.txt` and `EULA.txt`, neither of which exists either.

The test suite passes — it mocks every file access and every widget — so CI is green and the program still cannot start. Details and suggested fixes are in [`docs/internal/known-issues.md`](docs/internal/known-issues.md).

The template is sound and the customisation points are real; it needs its assets back.

## Key Features

- A `winver`-style window: logo, program name and version, trademark notice, licence blurb.
- **Open License** and **Open EULA** buttons that display the full text in their own windows.
- Importable as a function, so you can wire it to your own program's About menu.
- Python-Powered badge included.
- Pure standard library — Tkinter only.
- Cross-platform.

## Installation

```bash
git clone https://github.com/willtheorangeguy/ProgramVer
cd ProgramVer
python main.py
```

See [`docs/installation.md`](docs/installation.md), including what you need to supply before it runs.

## Usage

```python
from main import ProgramVer
ProgramVer()
```

Every string in the window is meant to be edited for your project — see [`docs/configuration.md`](docs/configuration.md).

## Documentation

Full documentation lives in [`docs/`](docs/index.md):
[Quickstart](docs/quickstart.md) · [Installation](docs/installation.md) · [Configuration](docs/configuration.md) · [Architecture](docs/architecture.md) · [Development](docs/development.md) · [Testing](docs/testing.md) · [FAQ](docs/faq.md) · [Troubleshooting](docs/troubleshooting.md) · [Roadmap](docs/roadmap.md)

## Support

Open a [GitHub Discussion](https://github.com/willtheorangeguy/ProgramVer/discussions), file an [issue](https://github.com/willtheorangeguy/ProgramVer/issues/new/choose), or join the [Discord](https://discord.gg/x3G8adwVUe).

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/willtheorangeguy/ProgramVer/compare).

See the org-wide [Contributing Guide](https://github.com/willtheorangeguy/.github/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://github.com/willtheorangeguy/.github/blob/main/CODE_OF_CONDUCT.md).

## Credits

This software uses the following open source packages, projects, services or websites:

<!-- Credits Table -->
<table>
  <tr>
    <th align="center"><img src="https://applets.imgix.net/https%3A%2F%2Fassets.ifttt.com%2Fimages%2Fchannels%2F2107379463%2Ficons%2Fmonochrome_large.png?w=240&h=240&s=8a19bbc158996d098e2fb18310ba7f33" width="150" height="150" alt="GitHub"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/182px-Python-logo-notext.svg.png" width="150" height="150" alt="PSF"/></th>
    <th align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Windows_logo_-_2021.svg/768px-Windows_logo_-_2021.svg.png" width="150" height="150" alt="Windows"/></th>
  </tr>
  <tr>
    <td align="center">GitHub</td>
    <td align="center">Python Software Foundation</td>
    <td align="center">Windows</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/">Web</a> - <a href="https://github.com/pricing">Plans</a></td>
    <td align="center"><a href="https://www.python.org/">Web</a> - <a href="https://psfmember.org/civicrm/contribute/transact?reset=1&id=2">Donate</a></td>
    <td align="center"><a href="https://www.microsoft.com/en-ca/windows">Web</a></td>
  </tr>
</table>

Sponsor [@willtheorangeguy](https://github.com/willtheorangeguy) on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US).

## License

MIT — see [`LICENSE.md`](LICENSE.md).

> Note the window itself currently displays a GPL blurb and a different copyright holder. That text is placeholder content meant to be replaced per project, but it does not match this repository's own licence — see [`docs/internal/known-issues.md`](docs/internal/known-issues.md).
