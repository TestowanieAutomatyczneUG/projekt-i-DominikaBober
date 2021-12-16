import sys
sys.path.append('./')
from packages import *
from all_games import AllGames


def main():

    for size in range(2,5):

        print(size)
        all_games = AllGames(size)
        with open(f'src/games/all_games_{size}.pickle', 'wb') as file:
            pickle.dump(all_games, file)
    

if __name__=="__main__":
    main()