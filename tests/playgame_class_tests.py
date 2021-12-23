import sys
sys.path.append('./')
from packages import *
from unittest.mock import patch

from src.play import PlayGame

class PlayTest(unittest.TestCase):


    @patch('builtins.input', side_effect=['new', 3, 3, 'exit'])
    # @patch('builtins.input', return_value='new')
    def test_sum_string_of_ints(self, mock_input):
        PlayGame()


unittest.main()