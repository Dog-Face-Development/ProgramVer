"""Internal utilities for ProgramVer."""

import os
import tkinter as tk


def get_or_create_root():
    """Detect whether a Tk root already exists.

    Returns:
        tuple: (window, is_standalone)
        - If Tk root exists: (Toplevel(root), False)
        - If no Tk root: (Tk(), True)
    """
    try:
        existing_root = tk._default_root
        if existing_root is not None and existing_root.winfo_exists():
            return tk.Toplevel(existing_root), False
    except Exception:
        pass
    root = tk.Tk()
    return root, True


def get_bundled_image_path(filename):
    """Get path to a bundled image in the programver package."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "imgs", filename)
