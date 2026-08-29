"""Core VersionDialog class for ProgramVer."""

# pylint: disable=too-few-public-methods, too-many-instance-attributes

import tkinter as tk

from programver._utils import get_or_create_root, get_bundled_image_path
from programver._text_viewer import TextViewer


class VersionDialog:
    """A customizable 'winver'-style version information dialog.

    Can be used standalone (creates its own Tk root and runs mainloop)
    or embedded in an existing tkinter application (uses Toplevel).

    The constructor is intentionally a flat, keyword-friendly bag of display
    options rather than a config object, so callers can construct it inline;
    `show()` is the only behaviour, by design.
    """

    def __init__(  # pylint: disable=too-many-arguments, too-many-positional-arguments
        self,
        app_name,
        version,
        copyright_text,
        license_path=None,
        eula_path=None,
        license_blurb=None,
        logo_path=None,
        show_python_powered=True,
        window_title=None,
    ):
        self.app_name = app_name
        self.version = version
        self.copyright_text = copyright_text
        self.license_path = license_path
        self.eula_path = eula_path
        self.license_blurb = license_blurb
        self.logo_path = logo_path
        self.show_python_powered = show_python_powered
        self.window_title = window_title or f"About {app_name}"

    def show(self):
        """Display the version dialog.

        If a Tk root already exists, creates a Toplevel window.
        If no Tk root exists, creates Tk root and calls mainloop().
        """
        window, is_standalone = get_or_create_root()
        window.title(self.window_title)

        if self.logo_path:
            logo_img = tk.PhotoImage(file=self.logo_path)
            # Keep a reference on the window so the image isn't garbage
            # collected before Tk draws it — the standard Tkinter idiom.
            window._logo_img = logo_img  # pylint: disable=protected-access
            logo_label = tk.Label(window, image=logo_img)
            logo_label.pack(side=tk.TOP)

        info = tk.Label(
            window, text=f"{self.app_name}\nVersion: {self.version}"
        )
        info.pack(side=tk.TOP)

        trademarks = tk.Label(window, text=self.copyright_text)
        trademarks.pack(side=tk.TOP)

        if self.license_blurb:
            blurb = tk.Label(window, text=self.license_blurb)
            blurb.pack(side=tk.TOP)

        if self.license_path:
            license_btn = tk.Button(
                window,
                text="Open License",
                command=lambda: TextViewer(window, "License", self.license_path),
            )
            license_btn.pack(pady=5)

        if self.eula_path:
            eula_btn = tk.Button(
                window,
                text="Open EULA",
                command=lambda: TextViewer(window, "EULA", self.eula_path),
            )
            eula_btn.pack(pady=5)

        if self.show_python_powered:
            badge_path = get_bundled_image_path("pythonpoweredlengthgif.gif")
            badge_img = tk.PhotoImage(file=badge_path)
            window._badge_img = badge_img  # pylint: disable=protected-access
            badge_label = tk.Label(window, image=badge_img)
            badge_label.pack(side=tk.BOTTOM)

        if is_standalone:
            window.mainloop()
