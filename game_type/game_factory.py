from game_type.short_game import ShortGame
from game_type.standard_game import StandardGame


class GameFactory:
    def create_game(self, game, dic):
        if game == "short":
            # letters, words = dictionary.init_game(short_game.NUM_LETTERS, short_game.MIN_LETTERS)
            return ShortGame(dic)
        if game == "standard":
            return StandardGame(dic)