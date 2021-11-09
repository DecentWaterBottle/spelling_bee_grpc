import json
import random


class Dictionary:
    _instance = None

    def __init__(self):
        if Dictionary._instance is None:
            Dictionary._instance = self
        else:
            raise Exception("Cannot instantiate more than one singleton")

    # ===================================================
    # FIND ALL PANGRAMS
    # ===================================================
    def find_pangrams(self, length):
        file = open("eng_dictionary/word_dictionary.json")
        data = json.load(file)
        words = []
        for word in data:
            if len(set(word)) == length and "s" not in word:
                words.append(word)
        return words

    # ===================================================
    # CHOOSE A RANDOM PANGRAM
    # ===================================================
    def choose_pangram(self, length):
        pangrams = self.find_pangrams(length)
        index = random.randrange(len(pangrams)-1)
        print(pangrams[index])
        return pangrams[index]

    # ===================================================
    # GENERATE UNIQUE LETTERS FROM PANGRAM
    # ===================================================
    def generate_letters(self, length):
        letters = []
        pangram = self.choose_pangram(length)
        for letter in pangram:
            if letter not in letters:
                letters.append(letter)
        return letters

    # ===================================================
    # GET ALL WORDS THAT CAN BE MADE FROM CHOSEN LETTERS
    # ===================================================
    def get_words(self, letters, min_length):
        file = open("eng_dictionary/word_dictionary.json")
        data = json.load(file)
        words = []
        for word in data:
            if all(item in letters for item in list(word)) and len(set(word)) <= len(letters) and \
                    "s" not in word and len(word) >= min_length:
                words.append(word)
        return words

    # ===================================================
    # INITIALIZE GAME
    # ===================================================
    def init_game(self, length, minimum_length):
        letters = self.generate_letters(length)
        words = self.get_words(letters, minimum_length)
        return letters, words
