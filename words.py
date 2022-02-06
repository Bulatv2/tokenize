# class Words

from tokenize import Tokenize
import re

class Words(Tokenize):
    """ делает токинезацию по словам """
    wordslist = []
    xlist = [" ", ""]
    onestring = ""
    getstring = ""
    def __init__(self, text):
        Tokenize.__init__(self, text)

    def load(self):
        """ токенизация по словам """
        self.getstring = Tokenize.load(self)
        self.onestring = re.sub("\.|\!|\,|\:|\;|\)|\(|\&|\#|\"|\?|\»|\«|\-", " ", self.getstring)
        self.wordslist = re.split("(\w+|[^a-zA-Z0-9])", self.onestring)
        self.filtered = [x for x in self.wordslist if x not in self.xlist]
        return self.filtered
