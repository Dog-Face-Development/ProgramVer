"""
Tests for ProgramVer main module.
Copyright (C) 2017-2024 Dog Face Development Co.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.
"""

# pylint: disable=import-error, invalid-name, unused-argument, wrong-import-position, import-outside-toplevel

import unittest
from unittest.mock import Mock, patch, mock_open
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import openLicense, openEULA, ProgramVer, get_resource_path


class TestGetResourcePath(unittest.TestCase):
    """Test cases for get_resource_path helper function."""

    def test_get_resource_path_returns_absolute_path(self):
        """Test that get_resource_path returns an absolute path."""
        result = get_resource_path("LICENSE.txt")
        self.assertTrue(os.path.isabs(result))

    def test_get_resource_path_includes_filename(self):
        """Test that get_resource_path includes the filename."""
        result = get_resource_path("LICENSE.txt")
        self.assertTrue(result.endswith("LICENSE.txt"))

    def test_get_resource_path_handles_subdirectories(self):
        """Test that get_resource_path handles subdirectories correctly."""
        result = get_resource_path("imgs/dfdlogo.gif")
        self.assertTrue("imgs" in result)
        self.assertTrue(result.endswith("dfdlogo.gif"))


class TestOpenLicense(unittest.TestCase):
    """Test cases for openLicense function."""

    @patch("main.Text")
    @patch("main.Tk")
    @patch(
        "builtins.open", new_callable=mock_open, read_data="GNU GENERAL PUBLIC LICENSE"
    )
    def test_openLicense_creates_window(self, mock_file, mock_tk, mock_text):
        """Test that openLicense creates a window and reads LICENSE.txt."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        openLicense()

        # Verify window was created
        mock_tk.assert_called_once()
        # Verify file was opened with absolute path
        mock_file.assert_called_once()
        call_args = mock_file.call_args[0]
        self.assertTrue(call_args[0].endswith("LICENSE.txt"))
        # Verify window title was set
        mock_window.title.assert_called_once_with("License")

    @patch("main.Tk")
    @patch("builtins.open", new_callable=mock_open, read_data="Test License Content")
    @patch("main.Text")
    def test_openLicense_displays_content(self, mock_text, mock_file, mock_tk):
        """Test that openLicense displays license content."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        openLicense()

        # Verify text widget was created with window
        mock_text.assert_called_once_with(mock_window)
        # Verify content was inserted
        mock_text_widget.insert.assert_called_once()
        # Verify widget was packed
        mock_text_widget.pack.assert_called_once()


class TestOpenEULA(unittest.TestCase):
    """Test cases for openEULA function."""

    @patch("main.Text")
    @patch("main.Tk")
    @patch(
        "builtins.open", new_callable=mock_open, read_data="END USER LICENSE AGREEMENT"
    )
    def test_openEULA_creates_window(self, mock_file, mock_tk, mock_text):
        """Test that openEULA creates a window and reads EULA.txt."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        openEULA()

        # Verify window was created
        mock_tk.assert_called_once()
        # Verify file was opened with absolute path
        mock_file.assert_called_once()
        call_args = mock_file.call_args[0]
        self.assertTrue(call_args[0].endswith("EULA.txt"))
        # Verify window title was set
        mock_window.title.assert_called_once_with("EULA")

    @patch("main.Tk")
    @patch("builtins.open", new_callable=mock_open, read_data="Test EULA Content")
    @patch("main.Text")
    def test_openEULA_displays_content(self, mock_text, mock_file, mock_tk):
        """Test that openEULA displays EULA content."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_text_widget = Mock()
        mock_text.return_value = mock_text_widget

        openEULA()

        # Verify text widget was created with window
        mock_text.assert_called_once_with(mock_window)
        # Verify content was inserted
        mock_text_widget.insert.assert_called_once()
        # Verify widget was packed
        mock_text_widget.pack.assert_called_once()


class TestProgramVer(unittest.TestCase):
    """Test cases for ProgramVer function."""

    @patch("main.Tk")
    @patch("main.PhotoImage")
    @patch("main.Label")
    @patch("main.Button")
    def test_programver_creates_window(
        self, mock_button, mock_label, mock_photoimage, mock_tk
    ):
        """Test that ProgramVer creates main window with all components."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_img = Mock()
        mock_photoimage.return_value = mock_img

        # Mock mainloop to prevent blocking
        mock_window.mainloop = Mock()

        ProgramVer()

        # Verify window was created
        mock_tk.assert_called_once()
        # Verify window title was set
        mock_window.title.assert_called_once()
        assert "ProgramVer" in str(mock_window.title.call_args)

    @patch("main.Tk")
    @patch("main.PhotoImage")
    @patch("main.Label")
    @patch("main.Button")
    def test_programver_loads_images(
        self, mock_button, mock_label, mock_photoimage, mock_tk
    ):
        """Test that ProgramVer loads required images."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_window.mainloop = Mock()

        ProgramVer()

        # Verify PhotoImage was called to load images
        assert mock_photoimage.call_count == 2
        # Check that both images are loaded with absolute paths
        calls = mock_photoimage.call_args_list
        image_files = [call[1]["file"] for call in calls]
        assert any("dfdlogo.gif" in img for img in image_files)
        assert any("pythonpoweredlengthgif.gif" in img for img in image_files)

    @patch("main.Tk")
    @patch("main.PhotoImage")
    @patch("main.Label")
    @patch("main.Button")
    def test_programver_creates_labels(
        self, mock_button, mock_label, mock_photoimage, mock_tk
    ):
        """Test that ProgramVer creates appropriate labels."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_window.mainloop = Mock()

        ProgramVer()

        # Verify Label was called multiple times
        assert mock_label.call_count >= 5
        # Verify labels were created with window

    @patch("main.Tk")
    @patch("main.PhotoImage")
    @patch("main.Label")
    @patch("main.Button")
    def test_programver_creates_buttons(
        self, mock_button, mock_label, mock_photoimage, mock_tk
    ):
        """Test that ProgramVer creates license and EULA buttons."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_window.mainloop = Mock()

        ProgramVer()

        # Verify Button was called for both buttons
        assert mock_button.call_count == 2
        # Verify buttons have correct text and commands
        calls = mock_button.call_args_list
        button_texts = [call[1]["text"] for call in calls]
        assert "Open License" in button_texts
        assert "Open EULA" in button_texts

    @patch("main.Tk")
    @patch("main.PhotoImage")
    @patch("main.Label")
    @patch("main.Button")
    def test_programver_button_commands(
        self, mock_button, mock_label, mock_photoimage, mock_tk
    ):
        """Test that buttons are linked to correct command functions."""
        mock_window = Mock()
        mock_tk.return_value = mock_window
        mock_window.mainloop = Mock()

        ProgramVer()

        calls = mock_button.call_args_list
        commands = [call[1].get("command") for call in calls]
        # Verify that openLicense and openEULA are set as commands
        assert openLicense in commands
        assert openEULA in commands


class TestModuleIntegration(unittest.TestCase):
    """Integration tests for the module."""

    def test_module_imports(self):
        """Test that the main module can be imported successfully."""
        import main

        assert hasattr(main, "ProgramVer")
        assert hasattr(main, "openLicense")
        assert hasattr(main, "openEULA")
        assert hasattr(main, "get_resource_path")

    def test_functions_are_callable(self):
        """Test that all exported functions are callable."""
        import main

        assert callable(main.ProgramVer)
        assert callable(main.openLicense)
        assert callable(main.openEULA)
        assert callable(main.get_resource_path)


if __name__ == "__main__":
    unittest.main()
