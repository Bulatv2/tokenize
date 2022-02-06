# class Tokenize

import re

class Tokenize:
    """ подготавливает текст для токенизаций. """
    lowertext = ""
    clearstring = ""
    onestring = ""
    def __init__(self, text):
        self.text = text

    def load(self):
        """ переводит текст в нижний регистр и заменяет \t\r\n символ " ". """
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t\r\n\f\v]", "", self.lowertext)
        self.onestring = re.sub("[ё]", "е", self.clearstring)
        return self.onestring
