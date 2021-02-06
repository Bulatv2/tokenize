# Class Punctuation

from tokenize import Tokenize
import re

class Punctuation(Tokenize):
    """ из списка делает токенизацию по символам """
    punclist = []
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по символам """
        self.getstring = Tokenize.load(self)
        self.punclist = re.split("" "(\W|[~«»<>,.?!-()])", self.getstring)
        print(self.punclist)
        return self.punclist
        
