# class Sentences

from tokenize import Tokenize
import re

class Sentences(Tokenize):
    """ сделать предложения """
    sentlist = []
    xlist = [" ", ""]
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по предложениям """
        self.getstring = Tokenize.load(self) 
        self.sentlist = re.split("(?<!\w\.\w.)(?<![a-z]\.)(?<=\.|\?|\!)(\s|[a-z].*)", self.getstring)
        self.filtered = [x for x in self.sentlist if x not in self.xlist]
        return self.filtered
