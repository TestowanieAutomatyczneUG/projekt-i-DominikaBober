import sys
sys.path.append('./')
from packages import *

from src.all_games import Game, AllGames

class GameTest(unittest.TestCase):

    @parameterized.expand([(2,), (3,), (4,)])
    def test_choice_in_all_games(self, size):
        all_games = []
        with open(f'tests/resources/all_games_{size}.txt','r+') as help:
            games = help.read().split("\n")
            for line in games[:-1]:
                all_games.append(ast.literal_eval(json.loads(line)))
        random_game = list(AllGames(size).get_one_game().values())[0].get_game_result()
        hamcrest.assert_that(random_game in all_games, hamcrest.is_(True))

unittest.main()