"""Entry point for python -m programver."""

import os
from programver.dialog import VersionDialog


def main():
    """Run ProgramVer demo dialog."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    license_path = os.path.join(base_dir, "..", "LICENSE.md")

    dialog = VersionDialog(
        app_name="ProgramVer",
        version="2.0.0",
        copyright_text=(
            "Copyright (C) 2017-2026 willtheorangeguy.\n"
            "All rights reserved."
        ),
        license_path=license_path,
        license_blurb=(
            "ProgramVer - A customizable version dialog for Python applications.\n"
            "This project is licensed under the MIT License."
        ),
        show_python_powered=True,
    )
    dialog.show()


if __name__ == "__main__":
    main()
