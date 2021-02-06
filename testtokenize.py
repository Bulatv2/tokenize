from sentences import Sentences
from words import Words
from punctuation import Punctuation

tlist = []

with open("data.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            tlist.append(row)
    varstring = "".join(tlist)

s = Sentences(varstring)
w = Words(varstring)
p = Punctuation(varstring)
s.load()
w.load()
p.load()
