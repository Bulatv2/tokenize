# class Words

from tokenize import Tokenize
import re

class Words(Tokenize):
    """ делает токинезацию по словам """
    wordslist = []
    getstring = ""
    onestring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по словам """
        self.getstring = Tokenize.load(self)
        self.onestring = re.sub("\.|\!|\,|\:|\;|\)|\(|\&|\#|\"|\?", "", self.getstring)
        self.wordslist = re.split("(\w+|[a-z])", self.onestring)
        print(self.wordslist)
        return self.wordslist
