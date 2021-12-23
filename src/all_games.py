import sys
sys.path.append('./')
from packages import *
from src.functions.print_table import print_table
from src.functions.create_game_plate import create_game_plate

def filter_function(game):

    columns = []
    zipped = zip(game[0],game[1])

    for game_row in game[2:]:
        zipped = [(*z, j) for z, j in zip(zipped, game_row)]

    columns = list(map(lambda col: list(set(col)), zipped))

    if len(sum(columns,[]))==len(game)**2:
        return True
    else:
        return False


class Game:

    def __init__(self,table):

        self.size = len(table)
        self.plate = table
        self.top_text, self.left_text, self.bottom_text, self.right_text = create_game_plate(self.plate)
    
    def get_game_result(self):

        return {"plate": self.plate, "top_text": self.top_text, "left_text": self.left_text,
                                "bottom_text": self.bottom_text, "right_text": self.right_text}
    
    def get_game(self, difficulty): # difficulty is int from 1 to 5

        difficulty_levels = {"1": 1, "2": 0.8, "3": 0.6, "4": 0.35, "5": 0.1}

        bars = {"plate": numpy.full((self.size, self.size), None), "top_text": self.top_text.copy(), "left_text": self.left_text.copy(),
                                "bottom_text": self.bottom_text.copy(), "right_text": self.right_text.copy()}

        temp = max(2,math.ceil(difficulty_levels[str(difficulty)]*self.size*4))
        while temp<self.size*4:
            
            temp_index = random.choice(numpy.where(numpy.array(bars['top_text']) != None)[0])
            bars['top_text'][temp_index] = None
            temp+=1
            if temp>=self.size*4:
                break
            temp_index = random.choice(numpy.where(numpy.array(bars['left_text']) != None)[0])
            bars['left_text'][temp_index] = None
            temp+=1
            if temp>=self.size*4:
                break
            temp_index = random.choice(numpy.where(numpy.array(bars['bottom_text']) != None)[0])
            bars['bottom_text'][temp_index] = None
            temp+=1
            if temp>=self.size*4:
                break
            temp_index = random.choice(numpy.where(numpy.array(bars['right_text']) != None)[0])
            bars['right_text'][temp_index] = None
            temp+=1
        
        return bars


class AllGames:

    def __init__(self, size: int):

        row = [i+1 for i in range(size)]
        perm = permutations(row)
        all_games = list(set(permutations(perm, size)))
        all_games = list(map(lambda num: list(num), all_games))
        all_games = list(map(lambda num: list(map(lambda nu: list(nu), num)), all_games))
        all_games = list(filter(filter_function, all_games))
        unique_games = unique(all_games)

        self.size = size
        self.games = list(map(lambda game: {str(uuid.uuid4()): Game(game)}, unique_games))
    
    def get_one_game(self):
        return random.choice(self.games)

    def get_all_games(self):
        return self.games
    
    def get_posible_results_for_game(self, game: dict): # game = AllGames(size).get_one_game()[id].get_game(difficulty)

        table, top_text, left_text, bottom_text, right_text = game.values()

        def equal_excetpt_none(list1, list2):
            return len(list1)==sum(list(map(lambda el1, el2: True if el1 is None else (int(el1)==el2), list1, list2)))
            
        def help(any_game):
            id = list(any_game.keys())[0]
            any_game_table, any_game_top_text, any_game_left_text, any_game_bottom_text, any_game_right_text = any_game[id].get_game_result().values()
            if equal_excetpt_none(top_text,any_game_top_text) and equal_excetpt_none(left_text,any_game_left_text) and equal_excetpt_none(bottom_text,any_game_bottom_text) and equal_excetpt_none(right_text,any_game_right_text):
                return True
            else:
                return False

        results = dict(ChainMap(*list(filter(help,self.games))))

        return results
