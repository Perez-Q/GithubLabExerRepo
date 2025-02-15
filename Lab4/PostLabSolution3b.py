import unittest
from unittest.mock import patch, call
import oxo_args_ui
import oxo_logic

class TestOxoArgsUI(unittest.TestCase):

    def test_get_menu_choice_valid(self):
        """Test that getMenuChoice returns a valid menu choice."""
        menu = ["Option 1", "Option 2", "Option 3"]
        with patch('builtins.input', side_effect=['2']):
            choice = oxo_args_ui.getMenuChoice(menu)
            self.assertEqual(choice, 2)

    def test_get_menu_choice_invalid_then_valid(self):
        """Test that getMenuChoice handles invalid input before valid input."""
        menu = ["Option 1", "Option 2", "Option 3"]
        with patch('builtins.input', side_effect=['0', '4', '2']):
            choice = oxo_args_ui.getMenuChoice(menu)
            self.assertEqual(choice, 2)

    def test_start_game(self):
        """Test that startGame creates a new game board."""
        game = oxo_args_ui.startGame()
        self.assertEqual(game, [" "] * 9)

    def test_resume_game(self):
        """Test that resumeGame restores a saved game."""
        with patch('oxo_logic.restoreGame', return_value=['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X']):
            game = oxo_args_ui.resumeGame()
            self.assertEqual(game, ['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X'])

    @patch('oxo_args_ui.print')
    def test_display_help(self, mock_print):
        """Test that displayHelp prints the correct help message."""
        oxo_args_ui.displayHelp()
        mock_print.assert_called_with('''
    Start new game:  starts a new game of tic-tac-toe
    Resume saved game: restores the last saved game and commences play
    Display help: shows this page
    Quit: quits the application
    ''')

    @patch('oxo_args_ui.quit', side_effect=SystemExit)
    def test_quit(self, mock_quit):
        """Test that quit raises SystemExit."""
        with self.assertRaises(SystemExit):
            oxo_args_ui.quit()
        mock_quit.assert_called_once()

    @patch('oxo_args_ui.playGame')
    def test_execute_choice_start_game(self, mock_playGame):
        """Test executeChoice for starting a new game."""
        with patch('oxo_args_ui.startGame', return_value=[" "] * 9):
            oxo_args_ui.executeChoice(1)
            mock_playGame.assert_called_once_with([" "] * 9)

    @patch('oxo_args_ui.playGame')
    def test_execute_choice_resume_game(self, mock_playGame):
        """Test executeChoice for resuming a saved game."""
        with patch('oxo_args_ui.resumeGame', return_value=['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X']):
            oxo_args_ui.executeChoice(2)
            mock_playGame.assert_called_once_with(['X', 'O', ' ', ' ', 'X', 'O', ' ', ' ', 'X'])

    @patch('oxo_args_ui.displayHelp')
    def test_execute_choice_display_help(self, mock_displayHelp):
        """Test executeChoice for displaying help."""
        oxo_args_ui.executeChoice(3)
        mock_displayHelp.assert_called_once()

    @patch('oxo_args_ui.quit', side_effect=SystemExit)
    def test_execute_choice_quit(self, mock_quit):
        """Test executeChoice for quitting the application."""
        with self.assertRaises(SystemExit):
            oxo_args_ui.executeChoice(4)
        mock_quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
