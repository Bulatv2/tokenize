from sentences import Sentences
from words import Words
from punctuation import Punctuation
import corpus

with open("somedata.txt", "r") as file:
    xstring = file.read()
stop = corpus.stopwords("russian")
sent = Sentences(xstring)
word = Words(xstring)
w = word.load()
punc = Punctuation(xstring)
filtered = [str(x) for x in w if x not in stop]
print(sent.load())
print(word.load())
print(filtered)
print(punc.load())
