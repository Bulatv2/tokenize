# class Sentences

from tokenize import Tokenize
import re

class Sentences(Tokenize):
    """ из списка сделать предложения """
    sentlist = []
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по предложениям """
        self.getstring = Tokenize.load(self) 
        self.sentlist = re.split("([.!?]+)", self.getstring)
        print(self.sentlist)
        return self.sentlist
