"""
Tests for ProgramVer package.
Copyright (C) 2017-2026 Dog Face Development Co.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
"""

# pylint: disable=import-error, invalid-name, wrong-import-position, import-outside-toplevel, unused-argument

import unittest
from unittest.mock import Mock, patch, mock_open, PropertyMock
import tkinter as tk


class TestVersionDialogInit(unittest.TestCase):
    """Test cases for VersionDialog.__init__."""

    def test_required_params_stored(self):
        """Test that required parameters are stored correctly."""
        from programver.dialog import VersionDialog

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
        )
        self.assertEqual(dialog.app_name, "TestApp")
        self.assertEqual(dialog.version, "1.0.0")
        self.assertEqual(dialog.copyright_text, "Copyright 2024")

    def test_optional_params_default_none(self):
        """Test that optional parameters default to None or expected values."""
        from programver.dialog import VersionDialog

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
        )
        self.assertIsNone(dialog.license_path)
        self.assertIsNone(dialog.eula_path)
        self.assertIsNone(dialog.license_blurb)
        self.assertIsNone(dialog.logo_path)
        self.assertTrue(dialog.show_python_powered)
        self.assertEqual(dialog.window_title, "About TestApp")

    def test_custom_window_title(self):
        """Test that custom window title is stored."""
        from programver.dialog import VersionDialog

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            window_title="Custom Title",
        )
        self.assertEqual(dialog.window_title, "Custom Title")

    def test_all_optional_params(self):
        """Test that all optional parameters are stored correctly."""
        from programver.dialog import VersionDialog

        dialog = VersionDialog(
            app_name="TestApp",
            version="2.0.0",
            copyright_text="Copyright 2024",
            license_path="/path/to/LICENSE",
            eula_path="/path/to/EULA",
            license_blurb="MIT License",
            logo_path="/path/to/logo.gif",
            show_python_powered=False,
            window_title="About Test",
        )
        self.assertEqual(dialog.license_path, "/path/to/LICENSE")
        self.assertEqual(dialog.eula_path, "/path/to/EULA")
        self.assertEqual(dialog.license_blurb, "MIT License")
        self.assertEqual(dialog.logo_path, "/path/to/logo.gif")
        self.assertFalse(dialog.show_python_powered)
        self.assertEqual(dialog.window_title, "About Test")


class TestVersionDialogShow(unittest.TestCase):
    """Test cases for VersionDialog.show method."""

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_standalone_calls_mainloop(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that show() calls mainloop in standalone mode."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        mock_window.mainloop.assert_called_once()

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_embedded_no_mainloop(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that show() does not call mainloop in embedded mode."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, False)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        mock_window.mainloop.assert_not_called()

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_sets_window_title(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that show() sets the window title."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            window_title="Custom Title",
            show_python_powered=False,
        )
        dialog.show()

        mock_window.title.assert_called_once_with("Custom Title")

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_creates_info_label(self, mock_root, mock_label, mock_photo, mock_path):
        """Test that show() creates an info label with app name and version."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="3.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        label_calls = mock_label.call_args_list
        label_texts = [call[1].get("text", "") for call in label_calls]
        self.assertTrue(
            any("TestApp" in t and "3.0.0" in t for t in label_texts)
        )

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_license_button_when_path_provided(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that license button appears when license_path is set."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            license_path="/path/to/LICENSE",
            show_python_powered=False,
        )
        dialog.show()

        button_texts = [call[1].get("text", "") for call in mock_button.call_args_list]
        self.assertIn("Open License", button_texts)

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_no_license_button_when_path_none(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that license button is hidden when license_path is None."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        button_texts = [call[1].get("text", "") for call in mock_button.call_args_list]
        self.assertNotIn("Open License", button_texts)

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_eula_button_when_path_provided(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that EULA button appears when eula_path is set."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            eula_path="/path/to/EULA",
            show_python_powered=False,
        )
        dialog.show()

        button_texts = [call[1].get("text", "") for call in mock_button.call_args_list]
        self.assertIn("Open EULA", button_texts)

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Button")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_no_eula_button_when_path_none(
        self, mock_root, mock_label, mock_button, mock_photo, mock_path
    ):
        """Test that EULA button is hidden when eula_path is None."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        button_texts = [call[1].get("text", "") for call in mock_button.call_args_list]
        self.assertNotIn("Open EULA", button_texts)

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_python_powered_badge(self, mock_root, mock_label, mock_photo, mock_path):
        """Test that Python Powered badge is shown when enabled."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=True,
        )
        dialog.show()

        mock_path.assert_called_once_with("pythonpoweredlengthgif.gif")

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_no_python_powered_badge(self, mock_root, mock_label, mock_photo, mock_path):
        """Test that Python Powered badge is hidden when disabled."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        mock_path.assert_not_called()

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_logo_when_provided(self, mock_root, mock_label, mock_photo, mock_path):
        """Test that logo is displayed when logo_path is provided."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            logo_path="/path/to/logo.gif",
            show_python_powered=False,
        )
        dialog.show()

        photo_calls = mock_photo.call_args_list
        logo_files = [call[1].get("file", "") for call in photo_calls]
        self.assertIn("/path/to/logo.gif", logo_files)

    @patch("programver.dialog.get_bundled_image_path", return_value="fake.gif")
    @patch("programver.dialog.tk.PhotoImage")
    @patch("programver.dialog.tk.Label")
    @patch("programver.dialog.get_or_create_root")
    def test_show_no_logo_when_not_provided(self, mock_root, mock_label, mock_photo, mock_path):
        """Test that no logo image is loaded when logo_path is None."""
        from programver.dialog import VersionDialog

        mock_window = Mock()
        mock_root.return_value = (mock_window, True)

        dialog = VersionDialog(
            app_name="TestApp",
            version="1.0.0",
            copyright_text="Copyright 2024",
            show_python_powered=False,
        )
        dialog.show()

        mock_photo.assert_not_called()


class TestTextViewer(unittest.TestCase):
    """Test cases for TextViewer read-only text window."""

    @patch("programver._text_viewer.tk.Text")
    @patch("programver._text_viewer.tk.Scrollbar")
    @patch("programver._text_viewer.tk.Frame")
    @patch("programver._text_viewer.tk.Toplevel")
    @patch("builtins.open", new_callable=mock_open, read_data="Test license content")
    def test_uses_toplevel_not_tk(
        self, mock_file, mock_toplevel, mock_frame, mock_scrollbar, mock_text
    ):
        """Test that TextViewer uses Toplevel, not Tk."""
        from programver._text_viewer import TextViewer

        mock_parent = Mock()
        mock_window = Mock()
        mock_toplevel.return_value = mock_window

        TextViewer(mock_parent, "License", "/path/to/file")

        mock_toplevel.assert_called_once_with(mock_parent)

    @patch("programver._text_viewer.tk.Text")
    @patch("programver._text_viewer.tk.Scrollbar")
    @patch("programver._text_viewer.tk.Frame")
    @patch("programver._text_viewer.tk.Toplevel")
    @patch("builtins.open", new_callable=mock_open, read_data="Test content")
    def test_sets_window_title(
        self, mock_file, mock_toplevel, mock_frame, mock_scrollbar, mock_text
    ):
        """Test that TextViewer sets the window title."""
        from programver._text_viewer import TextViewer

        mock_window = Mock()
        mock_toplevel.return_value = mock_window

        TextViewer(Mock(), "EULA", "/path/to/file")

        mock_window.title.assert_called_once_with("EULA")

    @patch("programver._text_viewer.tk.Text")
    @patch("programver._text_viewer.tk.Scrollbar")
    @patch("programver._text_viewer.tk.Frame")
    @patch("programver._text_viewer.tk.Toplevel")
    @patch("builtins.open", new_callable=mock_open, read_data="File contents here")
    def test_inserts_file_content(
        self, mock_file, mock_toplevel, mock_frame, mock_scrollbar, mock_text
    ):
        """Test that TextViewer inserts the file contents."""
        from programver._text_viewer import TextViewer

        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        TextViewer(Mock(), "License", "/path/to/file")

        mock_text_widget.insert.assert_called_once_with(tk.INSERT, "File contents here")

    @patch("programver._text_viewer.tk.Text")
    @patch("programver._text_viewer.tk.Scrollbar")
    @patch("programver._text_viewer.tk.Frame")
    @patch("programver._text_viewer.tk.Toplevel")
    @patch("builtins.open", new_callable=mock_open, read_data="Content")
    def test_text_is_disabled(
        self, mock_file, mock_toplevel, mock_frame, mock_scrollbar, mock_text
    ):
        """Test that TextViewer sets text widget to DISABLED (read-only)."""
        from programver._text_viewer import TextViewer

        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        TextViewer(Mock(), "License", "/path/to/file")

        mock_text_widget.config.assert_called_once_with(state=tk.DISABLED)

    @patch("programver._text_viewer.tk.Text")
    @patch("programver._text_viewer.tk.Scrollbar")
    @patch("programver._text_viewer.tk.Frame")
    @patch("programver._text_viewer.tk.Toplevel")
    @patch("builtins.open", new_callable=mock_open, read_data="Content")
    def test_scrollbar_is_attached(
        self, mock_file, mock_toplevel, mock_frame, mock_scrollbar, mock_text
    ):
        """Test that TextViewer creates and attaches a scrollbar."""
        from programver._text_viewer import TextViewer

        mock_sb = Mock()
        mock_scrollbar.return_value = mock_sb

        TextViewer(Mock(), "License", "/path/to/file")

        mock_sb.pack.assert_called_once()
        mock_sb.config.assert_called_once()


class TestGetOrCreateRoot(unittest.TestCase):
    """Test cases for get_or_create_root utility."""

    @patch("programver._utils.tk.Tk")
    @patch("programver._utils.tk._default_root", None)
    def test_creates_tk_when_no_root(self, mock_tk):
        """Test that a new Tk root is created when none exists."""
        from programver._utils import get_or_create_root

        mock_window = Mock()
        mock_tk.return_value = mock_window

        window, is_standalone = get_or_create_root()

        mock_tk.assert_called_once()
        self.assertTrue(is_standalone)

    @patch("programver._utils.tk.Toplevel")
    def test_creates_toplevel_when_root_exists(self, mock_toplevel):
        """Test that Toplevel is created when a root already exists."""
        from programver._utils import get_or_create_root

        mock_root = Mock()
        mock_root.winfo_exists.return_value = True
        mock_toplevel_window = Mock()
        mock_toplevel.return_value = mock_toplevel_window

        with patch("programver._utils.tk._default_root", mock_root):
            window, is_standalone = get_or_create_root()

        mock_toplevel.assert_called_once_with(mock_root)
        self.assertFalse(is_standalone)


class TestModuleIntegration(unittest.TestCase):
    """Integration tests for the package."""

    def test_package_imports(self):
        """Test that the programver package can be imported."""
        import programver

        self.assertTrue(hasattr(programver, "VersionDialog"))
        self.assertTrue(hasattr(programver, "__version__"))

    def test_version_dialog_is_class(self):
        """Test that VersionDialog is a class with a show method."""
        from programver import VersionDialog

        self.assertTrue(callable(VersionDialog))
        dialog = VersionDialog(
            app_name="Test", version="1.0", copyright_text="Copyright"
        )
        self.assertTrue(hasattr(dialog, "show"))
        self.assertTrue(callable(dialog.show))

    def test_version_string(self):
        """Test that __version__ is a string."""
        import programver

        self.assertIsInstance(programver.__version__, str)

    def test_main_module_imports(self):
        """Test that main.py's ProgramVer function is importable."""
        from main import ProgramVer

        self.assertTrue(callable(ProgramVer))


if __name__ == "__main__":
    unittest.main()
