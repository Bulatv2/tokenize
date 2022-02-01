# Class Punctuation

from tokenize import Tokenize
import re

class Punctuation(Tokenize):
    """ делает токенизацию по символам """
    punclist = []
    xlist = [" ", ""]
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по символам """
        self.getstring = Tokenize.load(self)
        self.punclist = re.split("\w+|[a-z])", self.getstring)
        self.filtered = [x for x in self.punclist if x not in self.xlist]
        return self.filtered
        
