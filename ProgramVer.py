# This is the standard program use by DFD Co. for versioning their products.
# Copyright (C) 2017 - 2018 Dog Face Development Co.

# Import Statements
from tkinter import *
window = Tk()

# Window Elements
window.title('Copyright & Version Info for ProgramVer') #change name based on program name
window.configure(bg='white')

# UI Elements
dfdimage = PhotoImage(file='dfdlogo.gif')
pythonimage = PhotoImage(file='pythonpoweredlengthgif.gif')
dfdlogo = Label(window, bg='white', image = dfdimage)
pythonpowered = Label(window, bg='white', image = pythonimage)
info = Label(window, bg='white', text='ProgramVer \n Version: BETA 0.0.1 (Build 1001)') #change respectively
trademarks = Label(window, bg='white', text='Copyright (C) 2017 - 2018 Dog Face Development Co. All rights reserved in all countries. \n ProgramVer and its code, user interface and all other associated trademarks are protected \nby trademarks and copyright in Canada, the United States and other countries.')
licenseblurb = Label(window, bg='white', text="""\n ProgramVer - Version window for DFD Co.'s programs
    Copyright (C) 2017-2018 Dog Face Development Company

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.""") #change as needed
licensebtn = Button(window, text='Open License', command=exit)

# Pack Statements
dfdlogo.pack(side=TOP)
info.pack(side=TOP)
trademarks.pack(side=TOP)
licenseblurb.pack(side=TOP)
licensebtn.pack(side=TOP)
pythonpowered.pack(side=BOTTOM)

# Maintain Window
window.mainloop()
