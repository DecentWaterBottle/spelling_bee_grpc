import random
import game
import copy
from game import Game
from dictionary import Dictionary


class EasyGame(Game):

    def __init__(self, dictionary):
        super().__init__()
        self.alphabet = copy.deepcopy(game.alphabet)
        self.letters = []
        self.words = []
        self.NUM_LETTERS = 6
        self.MIN_LETTERS = 3
        self.dic = dictionary

    def get_letters(self):
        self.letters = self.dic.generate_letters(self.NUM_LETTERS)

    def get_words(self):
        self.words = self.dic.get_words(self.letters, self.MIN_LETTERS)



