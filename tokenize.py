# class Tokenize

import re

class Tokenize:
    """ подготавливает текст для токенизаций. """
    lowertext = ""
    clearstring = ""
    def __init__(self, text):
        self.text = text

    def load(self):
        """ разбивка текста на символы. """
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t\r\n]", " ", self.lowertext)
        return self.clearstring
