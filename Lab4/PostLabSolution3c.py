import unittest
from unittest.mock import patch
import tkinter as tk
from oxo_gui_menu import buildMenu, dummy, top


class TestTicTacToeGUIMenu(unittest.TestCase):
    def setUp(self):
        """Set up the GUI for each test."""
        self.parent = tk.Tk()
        self.menu = buildMenu(self.parent)

    def tearDown(self):
        """Destroy the GUI instance after each test."""
        self.parent.destroy()

    def test_menu_structure(self):
        """Test that the menu structure is created correctly."""
        menu_labels = [self.menu.entrycget(i, "label") for i in range(self.menu.index("end") + 1)]
        self.assertListEqual(menu_labels, ["File", "Help"])

    def test_file_menu_items(self):
        """Test the items in the 'File' menu."""
        file_menu = self.menu.children["file"]
        file_labels = [file_menu.entrycget(i, "label") for i in range(file_menu.index("end") + 1)]
        self.assertListEqual(file_labels, ["New", "Resume", "Save", "Exit"])

    def test_help_menu_items(self):
        """Test the items in the 'Help' menu."""
        help_menu = self.menu.children["help"]
        help_labels = [help_menu.entrycget(i, "label") for i in range(help_menu.index("end") + 1)]
        self.assertListEqual(help_labels, ["Help", "About"])

    @patch("tkinter.messagebox.showinfo")
    def test_dummy_function(self, mock_showinfo):
        """Test that the dummy function shows an info message."""
        dummy()
        mock_showinfo.assert_called_once_with("Dummy", "Event to be done")

    def test_ev_exit(self):
        """Test that the 'Exit' menu command quits the application."""
        with self.assertRaises(SystemExit):  # Top-level `quit` raises a SystemExit
            top.quit()


if __name__ == "__main__":
    unittest.main()
