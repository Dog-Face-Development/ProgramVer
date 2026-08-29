"""Read-only scrollable text viewer window."""

# pylint: disable=too-few-public-methods

import tkinter as tk


class TextViewer:
    """Displays a file's contents in a read-only, scrollable Toplevel window.

    Intentionally has no public methods beyond construction: it builds and shows
    itself as a side effect of being instantiated, like a one-shot dialog helper.
    """

    def __init__(self, parent, title, file_path):
        self.window = tk.Toplevel(parent)
        self.window.title(title)

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        with open(file_path, "r", encoding="UTF-8") as f:
            content = f.read()

        text_widget.insert(tk.INSERT, content)
        text_widget.config(state=tk.DISABLED)
