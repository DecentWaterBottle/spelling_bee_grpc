import random
import game
import copy
from game import Game
from dictionary import Dictionary


class EasyGame(Game):

    def __init__(self):
        super().__init__()
        self.alphabet = copy.deepcopy(game.alphabet)
        self.letters = []
        self.pangrams = []
        self.pangram = ""
        self.NUM_LETTERS = 6
        self.dic = Dictionary()

    def get_pangrams(self):
        self.pangrams = self.dic.find_pangrams(self.NUM_LETTERS)






eg = EasyGame()
eg.get_pangrams()
eg.choose_pangram()
eg.generate_letters()
print(eg.letters)



