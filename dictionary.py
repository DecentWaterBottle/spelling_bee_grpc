import json
import random


class Dictionary:
    _instance = None

    def __init__(self):
        # self.pangram = ""
        self.letters = []
        if Dictionary._instance is None:
            Dictionary._instance = self
        else:
            raise Exception("Cannot instantiate more than one singleton")

    def find_pangrams(self, length):
        file = open("word_dictionary.json")
        data = json.load(file)
        words = []
        for word in data:
            counter = 0
            letters = []
            word_list = list(word)
            for letter in word_list:
                if letter not in letters:
                    letters.append(letter)
                    counter += 1
                if counter == length and letter == word_list[-1]:
                    words.append(word)
                    break
        return words

    def choose_pangram(self, length):
        pangrams = self.find_pangrams(length)
        index = random.randrange(len(pangrams)-1)
        return pangrams[index]

    def generate_letters(self, length):
        pangram = self.choose_pangram(length)
        for letter in pangram:
            if letter not in self.letters:
                self.letters.append(letter)
