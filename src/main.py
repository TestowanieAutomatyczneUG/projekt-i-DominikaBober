import sys
sys.path.append('./')
from packages import *
from src.all_games import AllGames


def main():

    for size in range(2,5):

        print(size)
        all_games = AllGames(size)
        with open(f'src/games/all_games_{size}.pickle', 'wb') as file:
            pickle.dump(all_games, file)

        with open(f'tests/resources/all_games_{size}.txt','w+') as help:
            help.writelines('%s\n' % json.dumps(line) for line in list(map(lambda game: str(list(game.values())[0].get_game_result()) ,all_games.get_all_games())))
            

if __name__=="__main__":
    main()