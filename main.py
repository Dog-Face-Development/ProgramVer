"""
ProgramVer - A Python version of Microsoft's 'winver'.
Copyright (C) 2017-2023 Dog Face Development Co.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os
from tkinter import *
# Import Statements

# Document Functions


def openLicense():
    windowl = Tk()
    licensefile = open("LICENSE.txt", "r")  # change file address as needed
    licensecontents = licensefile.read()
    licensefile.close()
    windowl.title("License")
    licensetext = Text(windowl)
    licensetext.insert(INSERT, licensecontents)
    licensetext.pack()


def openEULA():
    windowl = Tk()
    eulafile = open("EULA.txt", "r")  # change file address as needed
    eulacontents = eulafile.read()
    eulafile.close()
    windowl.title("EULA")
    eulatext = Text(windowl)
    eulatext.insert(INSERT, eulacontents)
    eulatext.pack()


# ProgramVer Function
def ProgramVer():
    window = Tk()
    # Window Elements
    window.title("Copyright & Version Info for ProgramVer"
                 )  # change name based on program name
    # UI Elements
    dfdimage = PhotoImage(file="imgs/dfdlogo.gif")
    pythonimage = PhotoImage(file="imgs/pythonpoweredlengthgif.gif")
    dfdlogo = Label(window, image=dfdimage)
    pythonpowered = Label(window, image=pythonimage)
    info = Label(
        window,
        text="ProgramVer \n Version: 1.9.0 (Build #)")  # change respectively
    trademarks = Label(
        window,
        text=
        "Copyright (C) 2017 - 2023 Dog Face Development Co. All rights reserved in all countries. \n ProgramVer and its code, user interface and all other associated trademarks are protected \nby trademarks and copyright in Canada, the United States and other countries.",
    )  # change as needed
    licenseblurb = Label(
        window,
        text="""\n ProgramVer - Version window for DFD Co.'s programs
        Copyright (C) 2017-2023 Dog Face Development Company

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, version 3 of the License.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License below for more details.""",
    )  # change as needed
    licensebtn = Button(window, text="Open License", command=openLicense)
    eulabtn = Button(window, text="Open EULA", command=openEULA)
    # Pack Statements
    dfdlogo.pack(side=TOP)
    info.pack(side=TOP)
    trademarks.pack(side=TOP)
    licenseblurb.pack(side=TOP)
    licensebtn.pack(pady=5)
    eulabtn.pack(pady=5)
    pythonpowered.pack(side=BOTTOM)
    # Maintain Window
    window.mainloop()
