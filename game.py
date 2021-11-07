from abc import ABC, abstractmethod

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class Game(ABC):

    def __init__(self):
        self.alphabet = alphabet

    @abstractmethod
    def get_letters(self):
        pass

    # @abstractmethod
    # def check_word(self):
    #     pass

    @abstractmethod
    def get_words(self):
        pass

