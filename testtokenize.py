from sentences import Sentences
from words import Words
from punctuation import Punctuation
import corpus
import countvector
"""
with open("data.txt", "r") as file:
    xstring = file.read()
"""
llist = []
rlist = []
with open("data.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)
            xstring = " ".join(llist)
stop = corpus.stopwords("russian")
#stemming = corpus.stem("russian")
#sent = Sentences(xstring)
word = Words(xstring)
w = word.load()
#punc = Punctuation(xstring)
stopfiltered = [str(x) for x in w if x not in stop]
#print(stopfiltered)
vect = countvector.vector(llist)
print(vect)
"""
for key, value in stemming.items():
    for i in range(len(stopfiltered)):
        if stopfiltered[i] == key:
            stopfiltered[i] = value
"""
"""
#print(sent.load())
#print(word.load())
print(stopfiltered)
#print(punc.load())
"""
