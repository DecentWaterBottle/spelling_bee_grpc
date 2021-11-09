from game_type.game_template import Game
import random
NUM_LETTERS = 6
MIN_LETTERS = 3


class ShortGame(Game):

    def __init__(self, dic):
        super().__init__()
        self.user_words = []
        self.score = 0
        self.letters, self.words = dic.init_game(NUM_LETTERS, MIN_LETTERS)
        self.main_letter = self.letters[random.randrange(len(self.letters))]
        self.letters.remove(self.main_letter)
        print(self.words)

    def check_word(self, word):
        word = word.lower()
        if word.isalpha() and self.main_letter in word and word not in self.user_words:
            if any(item in self.letters for item in list(word)) and word in self.words:
                self.calculate_score(word)
                self.user_words.append(word)
                return self.score, True
        return self.score, False

    def calculate_score(self, word):
        if len(word) == MIN_LETTERS:
            self.score += 1
        else:
            self.score += len(word)
        if all(item in self.letters for item in list(word)):
            self.score += 7

    def letters_to_string(self):
        temp_str = " "
        return temp_str.join(self.letters)

    def user_words_to_string(self):
        temp_str = " "
        print(temp_str.join(self.user_words))
        return temp_str.join(self.user_words)



