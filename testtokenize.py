from sentences import Sentences
from words import Words
from punctuation import Punctuation

with open("data.txt", "r") as file:
    xstring = file.read()

s = Sentences(xstring)
w = Words(xstring)
p = Punctuation(xstring)
print(s.load())
print(w.load())
print(p.load())
