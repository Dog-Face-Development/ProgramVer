<!-- Logo -->
<h1 align="center">
  <img src="https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/images/logo.png" height="250px" width="400px" alt="ProgramVer">
  <br>
  ProgramVer
  <br>
</h1>

<!-- Copy -->
<h4 align="center">A Python version of Microsoft's 'winver', built to be customizable, and to show copyright info and licenses.</h4>

<!-- Badges -->
<div align="center">
  <!-- Stability -->
  <img alt="PyPI Build State" src="https://github.com/Dog-Face-Development/ProgramVer/actions/workflows/push-to-pypi.yml/badge.svg">
  <!-- Stability -->
  <img alt="Pylint State" src="https://github.com/Dog-Face-Development/ProgramVer/actions/workflows/pylint.yml/badge.svg">
  <!-- CodeQL -->
  <img alt="CodeQL State" src="https://github.com/Dog-Face-Development/ProgramVer/actions/workflows/codeql-analysis.yml/badge.svg">
  <!-- Version -->
  <img alt="GitHub Version" src="https://img.shields.io/github/v/release/Dog-Face-Development/ProgramVer?include_prereleases">
  <!-- Issues -->
  <img alt="GitHub Issues" src="https://img.shields.io/github/issues/Dog-Face-Development/ProgramVer">
  <!-- Pull Requests -->
  <img alt="GitHub Pull Requests" src="https://img.shields.io/github/issues-pr/Dog-Face-Development/ProgramVer">
  <!-- Discord -->
  <img alt="Discord Server ID" src="https://img.shields.io/discord/1016437709247619092">
  <!-- Downloads -->
  <img alt="Downloads" src="https://img.shields.io/github/downloads/Dog-Face-Development/ProgramVer/total">
  <!-- Language Count -->
  <img alt="GitHub Languages" src="https://img.shields.io/github/languages/count/Dog-Face-Development/ProgramVer">
</div>

<!-- Navigation -->
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#download">Download</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#support">Support</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#changelog">Changelog</a> •
  <a href="#credits">Credits & Contributors</a>
</p>

<!-- Screenshot(s) -->
<div align="center">
    <img alt="Main image" src="https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/images/welcome.png">
</div>

## Key Features

* Display a version window.
* Can be called and imported as a function.
* Links to License text.
* Links to EULA text.
* Includes logo and Python Powered images.
* Cross platform.

## Download

You can **[download](https://github.com/Dog-Face-Development/ProgramVer/releases/latest) the source code** to run the scripts from the command line on Windows, macOS and Linux. **This will require [Python](https://www.python.org/downloads/).**

You can **[download](https://github.com/Dog-Face-Development/ProgramVer/releases/latest) the latest executable version** of ProgramVer for Windows. **This does not require Python.**

## How To Use

To run the application, you can use [Git and the Python Interpreter](https://github.com/Dog-Face-Development/ProgramVer/main/README.md#git), which allows you to clone and run the application, or [`pip`](https://github.com/Dog-Face-Development/ProgramVer/main/README.md#pip) to create a command line application.

### Git

To clone and run this application, you'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your computer. If you would rather not use Git, you can just download the script from GitHub above. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Dog-Face-Development/ProgramVer

# Go into the repository
$ cd ProgramVer

# Run the CLI
$ python main.py
```

### `pip`

You can install the program from the [Python Package Index](https://pypi.org/project/programver/) through `pip`.

```bash
# Install via pip
$ pip install programver

# Run the CLI
$ programver
```

However, you may want to add the version window to your program. To do so, follow these steps:

1. Download the latest source code release from [GitHub Releases](https://github.com/Dog-Face-Development/ProgramVer/releases/latest) page.
2. Extract the source code files using a program like [7-Zip](https://www.7-zip.org/).
3. Copy the `ProgramVer.py` file to your project's main directory.
4. Import ProgramVer by adding `from ProgramVer import *` to your Python `import` statements.
5. Call ProgramVer through the `ProgramVer()` function.
6. Enjoy your new version window!

## Support

Customization for ProgramVer can be found in the [`CUSTOMIZATION`](https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/CUSTOMIZATION.md) doc. More documentation is available in the **[Documentation](https://github.com/Dog-Face-Development/ProgramVer/tree/master/docs)** and on the **[Wiki](https://github.com/Dog-Face-Development/ProgramVer/wiki)**. If more support is required, please open a **[GitHub Discussion](https://github.com/Dog-Face-Development/ProgramVer/discussions)** or join our **[Discord](https://discord.gg/x3G8adwVUe)**.

## Contributing

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/Dog-Face-Development/ProgramVer/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us (including how to sign our CLA).

## Changelog

See the [`CHANGELOG`](CHANGELOG.md) file for details.

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

## Contributors

* [@willtheorangeguy](https://github.com/willtheorangeguy) - Sponsor on [PayPal](https://paypal.me/wvdg44?country.x=CA&locale.x=en_US)

## You may also like...

* [PyWorkout](https://github.com/Dog-Face-Development/PyWorkout) - A minimal CLI to keep you inspired during your workout!
* [PyAvatar](https://github.com/Dog-Face-Development/PyAvatar) - Easily display all of your creative avatars to keep them consistent across websites.
* [Periodic Table Info](https://github.com/Dog-Face-Development/Periodic-Table-Info) - Print all the elements in the Periodic Table of the Elements, with an interactive prompt to learn more.

## License

This project is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html) - see the [`LICENSE`](LICENSE.md) file for details. See the [Privacy Policy](https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/legal/PRIVACY.md), [Terms and Conditions](https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/legal/TERMS.md), and [EULA](https://github.com/Dog-Face-Development/ProgramVer/blob/master/docs/legal/EULA.md) for legal information.
