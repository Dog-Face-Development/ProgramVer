"""
ProgramVer - Standalone demo/test entry point.
Imports from the programver package and shows a demo version dialog.
Copyright (C) 2017-2026 willtheorangeguy
"""

# pylint: disable=import-error, invalid-name

import os
from programver import VersionDialog


def ProgramVer():
    """Main function for ProgramVer demo."""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    dialog = VersionDialog(
        app_name="ProgramVer",
        version="2.0.0",
        copyright_text=(
            "Copyright (C) 2017-2026 Dog Face Development Co.\n"
            "All rights reserved in all countries.\n"
            "ProgramVer and its code, user interface and all other associated\n"
            "trademarks are protected by trademarks and copyright in Canada,\n"
            "the United States and other countries."
        ),
        license_path=os.path.join(base_dir, "LICENSE.md"),
        license_blurb=(
            "\nProgramVer - Version window for DFD Co.'s programs\n"
            "Copyright (C) 2017-2026 Dog Face Development Company\n\n"
            "This program is free software: you can redistribute it and/or modify\n"
            "it under the terms of the GNU General Public License as published by\n"
            "the Free Software Foundation, version 3 of the License.\n\n"
            "This program is distributed in the hope that it will be useful,\n"
            "but WITHOUT ANY WARRANTY; without even the implied warranty of\n"
            "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the\n"
            "GNU General Public License below for more details."
        ),
        show_python_powered=True,
        window_title="Copyright & Version Info for ProgramVer",
    )
    dialog.show()


if __name__ == "__main__":
    ProgramVer()
