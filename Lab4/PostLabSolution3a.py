import os
import unittest
from oxo_data import saveGame, restoreGame, _getPath

class TestOxoData(unittest.TestCase):
    def setUp(self):
        """Set up a temporary test file and backup the original game file."""
        self.test_file = os.path.join(_getPath(), "oxogame.dat")
        self.backup_file = self.test_file + ".backup"

        # Backup the original file if it exists
        if os.path.exists(self.test_file):
            os.rename(self.test_file, self.backup_file)

    def tearDown(self):
        """Restore the original game file after testing."""
        if os.path.exists(self.backup_file):
            if os.path.exists(self.test_file):
                os.remove(self.test_file)
            os.rename(self.backup_file, self.test_file)
        elif os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_restore_game(self):
        """Test saving and restoring a game."""
        game_state = ["X", "O", " ", "X", "O", " ", "X", " ", "O"]

        # Save the game state
        saveGame(game_state)

        # Restore the game state
        restored_game = restoreGame()

        # Check that the restored game matches the original
        self.assertEqual(game_state, restored_game)

    def test_restore_game_empty_file(self):
        """Test restoring a game when the file is empty."""
        # Create an empty file
        with open(self.test_file, 'w') as f:
            pass

        # Attempt to restore the game
        restored_game = restoreGame()

        # Check that the restored game is an empty list
        self.assertEqual(restored_game, [])

    def test_save_game_creates_file(self):
        """Test that saving a game creates the file."""
        game_state = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

        # Save the game state
        saveGame(game_state)

        # Check that the file exists
        self.assertTrue(os.path.exists(self.test_file))

if __name__ == "__main__":
    unittest.main()
