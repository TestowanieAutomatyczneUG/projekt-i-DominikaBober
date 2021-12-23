import sys
sys.path.append('./')
from packages import *
from unittest.mock import patch
warnings.filterwarnings("ignore")

from src.play import PlayGame

class PlayGameTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['exit'])
    def test_start_game_by_exit(self, mock_input):
        game = PlayGame()

# new game
    @patch('builtins.input', side_effect=['new', '3', '3', 'exit'])
    def test_new_game_and_exit(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '6', '5', '6', '5', '9', 'exit'])
    def test_new_game_bad_size(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '6', '3', '5', '3', '6', '3', '5', '3', '9', 'exit'])
    def test_new_game_bad_difficulty(self, mock_input):
        game = PlayGame()

    # testing add
    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '1', '1', '3', 'exit'])
    def test_new_game_add_through_input(self, mock_input):
        game = PlayGame()
    
    @patch('builtins.input', side_effect=['new', '3', '3', 'exit'])
    def test_new_game_add_through_module(self, mock_input):
        game = PlayGame()
        plate = game.put_value(1, 1, 3)
        hamcrest.assert_that(plate[0][0], hamcrest.equal_to(3))
    
        # bad column
    @patch('builtins.input', side_effect=['new', '3', '3', 'add', 'bad_col', 'exit'])
    def test_new_game_add_bad_col_str(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '0', 'exit'])
    def test_new_game_add_bad_col_lower_int(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '4', 'exit'])
    def test_new_game_add_bad_col_upper_int(self, mock_input):
        game = PlayGame()
    
    @patch('builtins.input', side_effect=['new', '3', '3', 'exit'])
    def test_new_game_add_bad_col_through_module(self, mock_input):
        game = PlayGame()
        game.put_value(5, 1, 3)
    
        # bad row
    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', 'bad_row', 'exit'])
    def test_new_game_add_bad_row_str(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '0', 'exit'])
    def test_new_game_add_bad_row_lower_int(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '4', 'exit'])
    def test_new_game_add_bad_row_upper_int(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'exit'])
    def test_new_game_add_bad_row_through_module(self, mock_input):
        game = PlayGame()
        game.put_value(1, 5, 3)
          
        # bad value
    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '2', 'bad_value', 'exit'])
    def test_new_game_add_bad_value_str(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '2', '0', 'exit'])
    def test_new_game_add_bad_value_lower_int(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '2', '4', 'exit'])
    def test_new_game_add_bad_value_upper_int(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'exit'])
    def test_new_game_add_bad_value_through_module(self, mock_input):
        game = PlayGame()
        game.put_value(1, 1, 5)
          
    # testing undo
    @patch('builtins.input', side_effect=['new', '3', '3', 'undo', 'exit'])
    def test_new_game_undo_before_move(self, mock_input):
        game = PlayGame()

    @patch('builtins.input', side_effect=['new', '3', '3', 'add', '2', '2', '2', 'undo', 'exit'])
    def test_new_game_undo_after_add(self, mock_input):
        game = PlayGame()
        

# load game
    @patch('builtins.input', side_effect=['save', 'test_save_1', 'exit'])
    # This game looks like this
    # +---+---+---+---+---+
    # |   |   | 1 | 2 |   |
    # +---+---+---+---+---+
    # | 2 |   | 3 |   | 2 |
    # +---+---+---+---+---+
    # |   |   |   |   |   |
    # +---+---+---+---+---+
    # | 1 | 3 |   |   | 3 |
    # +---+---+---+---+---+
    # |   |   | 2 | 2 |   |
    # +---+---+---+---+---+ 
    def test_load_game_and_exit(self, mock_input):
        game = PlayGame()

    # testing add
    @patch('builtins.input', side_effect=['save', 'test_game_1', 'add', '2', '3', '3', 'exit'])
    def test_load_game_and_add(self, mock_input):
        game = PlayGame()
    
    if "test_game_2" in list(map(lambda save: save[:save.index(".pickle")], os.listdir("src/saves"))):
        test_load_game_add_and_save_side_effect = ['save', 'test_game_1', 'add', '2', '3', '3', 'save', 'test_game_2', 'y', 'exit']
    else:
        test_load_game_add_and_save_side_effect = ['save', 'test_game_1', 'add', '2', '3', '3', 'save', 'test_game_2', 'exit']
    @patch('builtins.input', side_effect=test_load_game_add_and_save_side_effect)
    def test_load_game_add_and_save(self, mock_input):
        game = PlayGame()
    
    # testing undo
    @patch('builtins.input', side_effect=['save', 'test_game_1', 'undo', 'exit'])
    def test_load_game_undo(self, mock_input):
        game = PlayGame()
    
    # testing undo move
    @patch('builtins.input', side_effect=['save', 'test_game_1', 'undo move', '1', '3', 'exit'])
    def test_load_game_undo_made_move(self, mock_input):
        game = PlayGame()
                
    @patch('builtins.input', side_effect=['save', 'test_game_1', 'undo move', '2', '2', 'exit'])
    def test_load_game_undo_unmade_move(self, mock_input):
        game = PlayGame()

save_stdout = sys.stdout
sys.stdout = open('trash', 'w')
unittest.main()
sys.stdout = save_stdout
