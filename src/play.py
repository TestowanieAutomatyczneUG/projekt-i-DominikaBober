import sys
sys.path.append('./')
from packages import *
warnings.filterwarnings("ignore")

from functions.print_table import print_table
from all_games import AllGames

def filter_posible_results_for_game(plate, results):

    def filter_plates(result, res_key):
        result_plate = result.get_game_result()["plate"]
        # print(list(itertools.chain(*plate)), res_key, list(itertools.chain(*result_plate)))
        # print_table(result_plate, result.get_game_result()["top_text"], result.get_game_result()["left_text"], result.get_game_result()["bottom_text"], result.get_game_result()["right_text"])
        if len(list(itertools.chain(*plate)))==sum(list(map(lambda el1, el2: True if el1 is None or el1=="" else (int(el1)==el2), 
                                                    list(itertools.chain(*plate)), list(itertools.chain(*result_plate))))):
            return True
        else:
            return False
            
    posible_results = list(filter(None,list(map(lambda res_key, res_game: res_key if filter_plates(res_game, res_key) else None, 
                                        list(results.keys()), list(results.values())))))
    return posible_results




class PlayGame:

    def __init__(self, size, difficulty):

        with open(f'src/games/all_games_{size}.pickle', 'rb') as file:
            all_games = pickle.load(file)

        game = all_games.get_one_game()
        id = list(game.keys())[0]
        self.game = game[id].get_game(difficulty)
        self.posible_results = all_games.get_posible_results_for_game(self.game)
        self.posible_results_ids = list(self.posible_results.keys())
        self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text = self.game.values()
        self.size = size
        self.last_move = ()

        print("There is your board game. To write down an answer write in console \u001b[34madd\u001b[0m, it will ask you for coordinates and value. To cancel your last move write in concole \u001b[34mundo\u001b[0m. To get possible actions write in console \u001b[34mhelp\u001b[0m.")
        print_table(self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text)
    
    def put_value(self, col, row, value):            

        # try:
            if value is None or (type(value) is int and 1<=value<=self.size):
                self.plate[row-1, col-1] = value
                self.last_move = (row, col)
                self.posible_results_ids = filter_posible_results_for_game(self.plate, self.posible_results)
                if len(self.posible_results_ids)==0:
                    temp_plate = self.plate.copy()
                    temp_plate[row-1, col-1] = f"{Fore.RED}{value}{Style.RESET_ALL}"
                    print_table(temp_plate, self.top_text, self.left_text, self.bottom_text, self.right_text)
                    print("Your last move was wrong")
                else:
                    print_table(self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text)
            else:
                print("Bledna wartosc")

        # except TypeError:
        #     print("Bledne wspolzedne")
    
    def undo(self):
        try:
            # self.plate[self.last_move[0]][self.last_move[1]] = ""
            # # print(list(filter(lambda dict_key, dict_val: {dict_key: dict_val}, self.posible_results)))
            # temp_posible_results = dict(ChainMap(*list(map(lambda dict_key, dict_val: {dict_key: dict_val} if dict_key in self.posible_results_ids else None, 
            #                     list(self.posible_results.keys()), list(self.posible_results.values())))))
            
            # self.posible_results_ids = filter_posible_results_for_game(self.plate, temp_posible_results)
            # print_table(self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text)
            self.put_value(self.last_move[1], self.last_move[0], None)
        except IndexError:
            print("There is no move to undo")
    
    def undo_move(self, row, col):
        try:
            self.put_value(col, row, None)
        except TypeError:
            print("Bledne wspolzedne")

        



def main():
    
    

    # your_game = all_games.get_one_game()
    # id = list(your_game.keys())[0]
    # gg = your_game[id].get_game(5)
    # results = all_games.get_posible_results_for_game(gg)

    play = PlayGame(3, 4)
    play.put_value(1,1,3)
    play.undo()
    play.put_value(1,1,2)



if __name__=="__main__":
    main()