"""Word Finder: finds random words from a dictionary."""
from random import randrange


class WordFinder:
    ...
    def __init__ (self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as words_list:
            self.words_list = list(words_list)

    def num_of_words_read(self):
        return len(self.words_list)

    def random_word(self):
        random_index = randrange(0,self.num_of_words_read())
        return self.words_list[random_index].rstrip('\n')

class SpecialWordFinder(WordFinder):
    def __init__(self, file_path):
        super().__init__(file_path)

    def random_word(self):
        while(True):
            random_word = super().random_word()
            if random_word[0] != '#':
                out = random_word
                break
        return out




new_inst = SpecialWordFinder('words.txt')