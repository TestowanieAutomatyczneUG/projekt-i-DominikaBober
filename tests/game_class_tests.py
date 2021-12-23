import sys
sys.path.append('./')
from packages import *

from src.all_games import Game

def equal_excetpt_none(list1, list2):
    return len(list1)==sum(list(map(lambda el1, el2: True if el1 is None else el1==el2, list1, list2)))

class GameTest(unittest.TestCase):
    
    def testInstance(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        game = Game(plate)
        assert_that(game).is_instance_of(Game)

    # get_game_result
    def test_get_game_result_keys(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        game_keys = ["plate", "top_text", "left_text", "bottom_text", "right_text"]
        game = Game(plate)
        assert_that(list(game.get_game_result().keys())).is_equal_to(game_keys)

    def test_get_game_result_plate(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        game = Game(plate)
        assert_that(game.get_game_result()["plate"]).is_equal_to(plate)

    def test_get_game_result_top_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        top_text = [3, 2, 1]
        game = Game(plate)
        assert_that(game.get_game_result()["top_text"]).is_equal_to(top_text)

    def test_get_game_result_left_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        left_text = [3, 2, 1]
        game = Game(plate)
        assert_that(game.get_game_result()["left_text"]).is_equal_to(left_text)

    def test_get_game_result_bottom_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        bottom_text = [1, 2, 2]
        game = Game(plate)
        assert_that(game.get_game_result()["bottom_text"]).is_equal_to(bottom_text)

    def test_get_game_result_right_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        right_text = [1, 2, 2]
        game = Game(plate)
        assert_that(game.get_game_result()["right_text"]).is_equal_to(right_text)
    
    def test_get_game_result(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        game = Game(plate)
        assert_that(game.get_game_result()).is_equal_to(result)

    # get_game
    def test_get_game_keys(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        game_keys = ["plate", "top_text", "left_text", "bottom_text", "right_text"]
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        assert_that(list(game_set.keys())).is_equal_to(game_keys)

    def test_get_game_top_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        assert_that(True==equal_excetpt_none(game_set['top_text'], result['top_text'])).is_true()

    def test_get_game_left_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        assert_that(True==equal_excetpt_none(game_set['left_text'], result['left_text'])).is_true()

    def test_get_game_bottom_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        assert_that(True==equal_excetpt_none(game_set['bottom_text'], result['bottom_text'])).is_true()

    def test_get_game_right_text(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        assert_that(True==equal_excetpt_none(game_set['right_text'], result['right_text'])).is_true()

    def test_get_game(self):
        plate = [[1, 2, 3],[2, 3, 1],[3, 1, 2]]
        result = {'plate': [[1, 2, 3], [2, 3, 1], [3, 1, 2]], 
                    'top_text': [3, 2, 1], 'left_text': [3, 2, 1],
                    'bottom_text': [1, 2, 2], 'right_text': [1, 2, 2]}
        difficulty = 3
        game = Game(plate)
        game_set = game.get_game(difficulty)
        is_okey = True
        for key in list(result.keys())[1:]:
            is_okey = is_okey and True==equal_excetpt_none(game_set[key], result[key])

        assert_that(is_okey).is_true()
    

unittest.main()