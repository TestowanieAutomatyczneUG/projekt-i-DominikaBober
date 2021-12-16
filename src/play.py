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

    def __init__(self):

        print(f"{Fore.GREEN}-----WELCOME TO THE GAME-----{Style.RESET_ALL}")
        game = input("If you want to start new game write \u001b[34mnew\u001b[0m. If you want to load game from save file write \u001b[34msave\u001b[0m")

        tres = 0
        good_to_go = False
        while tres<5 and good_to_go != True:
            try:
                self.size = int(input("Choose game size 2, 3 or 4 "))
                if self.size not in [2, 3, 4]:
                    raise ValueError
                difficulty = int(input("Choose game difficulty 1, 2, 3, 4 or 5 "))
                if difficulty not in [1, 2, 3, 4, 5]:
                    raise ValueError
                good_to_go = True
            except ValueError:
                tres+=1
                print("Wrong values")

        if tres==5:
            print("Too many wrong values given. Game ends.")
        else:
            with open(f'src/games/all_games_{self.size}.pickle', 'rb') as file:
                all_games = pickle.load(file)

            game = all_games.get_one_game()
            id = list(game.keys())[0]
            self.game = game[id].get_game(difficulty)
            self.posible_results = all_games.get_posible_results_for_game(self.game)
            self.posible_results_ids = list(self.posible_results.keys())
            self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text = self.game.values()
            self.last_move = ()
            self.is_game_on = True

            help = "To read game rules write in console \u001b[34mrules\u001b[0m. To write down an answer write in console \u001b[34madd\u001b[0m, it will ask you for coordinates and value. To cancel your last move write in console \u001b[34mundo\u001b[0m. To cancel any move write in console \u001b[34mundo move\u001b[0m. To solve your game write in console \u001b[34msolve\u001b[0m. To play a new game write in console \u001b[34mnew game\u001b[0m. To save your current game write in console \u001b[34msave\u001b[0m. To get possible actions write in console \u001b[34mhelp\u001b[0m."
            print(f"There is your board game. {help}\n")
            print_table(self.plate, self.top_text, self.left_text, self.bottom_text, self.right_text)

            def handle_add():
                try:
                    col = int(input("To which column? \n"))
                    row = int(input("To which row? \n"))
                    value = int(input("What value? \n"))
                    self.put_value(col, row, value)
                except ValueError:
                    print("Wrong value type")
            
            def handle_undo():
                self.undo()

            def handle_undo_move():
                try:
                    col = int(input("Which column? \n"))
                    row = int(input("Which row? \n"))
                    self.undo_move(row, col)
                except ValueError:
                    print("Wrong value type")
            
            def handle_help():
                print(help)
            
            def handle_solve():
                self.solve_game()
            
            def handle_save():
                save_name = input("Under what name you wonna save this game? ").replace(" ", "_")
                if set(save_name).difference(ascii_letters).difference("_") == set():
                    with open(f'src/saves/{save_name}.pickle', 'wb') as file:
                        pickle.dump(self, file)
                else:
                    print("Wrong save name")

            while self.is_game_on:

                all_options = {"add": handle_add, "undo": handle_undo, "undo move": handle_undo_move, "rules": self.how_to_play,
                                "solve": handle_solve, "help":handle_help, "exit": self.handle_exit, "new game": self.handle_new_game,
                                "save": handle_save}

                try:
                    option = input("What you wonna do now?\n")
                    all_options[option]()

                except KeyError:
                    print(f"Command not found. {help}\n")


    def put_value(self, col, row, value):            
        try:
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
                    if len(list(filter(None,list(itertools.chain(*self.plate)))))==self.size**2:
                        print(f"{Fore.GREEN}---CONGRATULATIONS YOU WON THE GAME---{Style.RESET_ALL}")
                        print("If you would like to start new game write \u001b[34mstart\u001b[0m.")
                        print("If you wonna live write \u001b[34mexit\u001b[0m.\n")
                        move = input()
                        if move == "start":
                            self.handle_new_game()
                        elif move == "exit":
                            self.handle_exit()
                        else:
                            print("Don't know what did you mean, but...")
                            self.handle_exit()
            else:
                print("Wrong value")
        except TypeError:
            print("Wrong coordinates")

    
    def undo(self):
        try:
            self.put_value(self.last_move[1], self.last_move[0], None)
        except IndexError:
            print("There is no move to undo")

    
    def undo_move(self, row, col):
        try:
            self.put_value(col, row, None)
        except TypeError:
            print("Wrong coordinates")

    
    def solve_game(self):
        try:
            solution = self.posible_results[self.posible_results_ids[0]]
            print("There is the solution:")
            print_table(solution.get_game_result()["plate"], self.top_text, self.left_text, self.bottom_text, self.right_text)
        except IndexError:
            print("There is no sotution for values that you put")
    
    def handle_exit(self):
        print("Thanks for plaing!\n")
        self.is_game_on = False
    
    def handle_new_game(self):
        print(f"{Fore.GREEN}-----NEW GAME-----{Style.RESET_ALL}")
        self.__init__()
    
    def how_to_play(self):

        print(f"Below you have example of the game. In the board game table you have {Style.NORMAL}{Fore.MAGENTA}pink{Style.RESET_ALL} numbers which tell you how many pyramids is visable from that view, white numbers symbolise pyramid height.\n In this picture is \"in real live\" example of the game.")
        print('''
                O\t\t  /\ \t\t\t\t\tO
                |\t\t /__\ \t\t\t /\ 		|
                /\ \t\t/____\ \t\t/\ \t/__\		/\ \n''')
        print("Person on the left sees one pyramid. Person on the rigth sees two pyramids. From these informations we can tell heights of the pyramids. In the table it would look like this:\n")
        print(BeautifulTable().append_row([f"{Fore.MAGENTA}1{Style.RESET_ALL}", 3, 1, 2, f"{Fore.MAGENTA}2{Style.RESET_ALL}"]),"\n")
        print("Now lest see solution for this game 3x3")
        print_table(numpy.full((3, 3), None), [3, 1, None], [2, None, 1], [1, 2, None], [2, None, 3])
        print("--SOLUTION--")
        print_table([[1, 3, 2], [2, 1, 3], [3, 2, 1]], [3, 1, None], [2, None, 1], [1, 2, None], [2, None, 3])
        print("Hope it helps!")
    
        


def main():

    PlayGame()





if __name__=="__main__":
    main()
