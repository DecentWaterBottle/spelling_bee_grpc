from abc import ABC, abstractmethod


class Game(ABC):

    @abstractmethod
    def check_word(self, word):
        pass

    @abstractmethod
    def calculate_score(self, word):
        pass

    @abstractmethod
    def letters_to_string(self):
        pass

    @abstractmethod
    def user_words_to_string(self):
        pass



