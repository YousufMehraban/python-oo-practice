

# from os import read
from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        """read a file, initialize a list and print number of word read"""
        self.word = open(file, 'r')
        self.lst = self.MakeList(self.word)
        print(f'{len(self.lst)} words read')

    def random(self):
        """return random item from a list"""
        return choice(self.lst).strip()

    def MakeList(self, iterable):
        """return a list from an iterable"""
        return [word.strip() for word in iterable]

    def __repr__(self) -> str:
        return f'<WordFinder: {len(self.lst)} words read)>'


class SpecialWordFinder(WordFinder):
    """spcial word finder that excludes empty strings/items and comments """
    def __init__(self, file):
        super().__init__(file)

    def MakeList(self, iterable):
        """creates a list from an iterable and excludes empty strings/items and comments """
        return [word.strip() for word in iterable if word.strip() and not word.startswith('#')]

    def __repr__(self) -> str:
        return f'<SpecialWordFinder: {len(self.lst)} words read: excludes empty string & comments>'