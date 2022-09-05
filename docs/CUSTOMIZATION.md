# ProgramVer Customization

ProgramVer is designed to be highly customizable, in order to make the version window suit each individual project. The license and EULA texts can be changed, as well as the program name, version number and more.

All of these instructions require [a text editor](https://code.visualstudio.com/) to be installed.

## Set the License File and Text

The version window can be configured to use a custom license file and text.

1. _Line 11_: Replace the `'LICENSE.txt'` with the name (or path) to the license file.
2. _Line 40_: Replace the text in between the single quotes (`'...'`) with the trademark/license blurb. For example, here is the one from `winver.exe`:

```text
© Microsoft Corporation. All rights reserved.
```

3. _Line 41_: Replace the text in between the triple double quotes (`"""..."""`) with the license blurb, if your license includes this. For example, the GNU Public License includes a section of text that should be included with each program:

```text
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## Set the EULA File

The version window can be configured to use a custom EULA file.

1. _Line 21_: Replace the `'EULA.txt'` with the name (or path) to the End User License Agreement file.

## Set the Window Title

The version window can be configured to have a custom title.

1. _Line 33_: Replace the `'Copyright & Version Info for ProgramVer'` with the name of the project ProgramVer is being added to.
2. _Line 39_: Replace the `'ProgramVer \n Version: 1.8.0 (Build 1080)'` with the program name and the version number.

## Set the Images

The version window can be configured to show a company logo and the Python Powered logo.

1. _Line 35_: Replace the `'dfdlogo.gif'` with the name (or path) of the company logo image.
2. _Line 36_: Replace the `'pythonpoweredlengthgif.gif'` with the name (or path) to another Python Powered image, or any other image that fits.
