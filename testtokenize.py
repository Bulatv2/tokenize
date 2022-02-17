from sentences import Sentences
from words import Words
from punctuation import Punctuation
import corpus

nlist = []

# для избежания возможной ошибки при неправильном форматировании данных
with open("data.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row)
        varstring = " ".join(xlist)

w = Words(varstring)
wl = w.load()
print(wl)
stop = corpus.stopwords("russian")
print(stop)
for i in wl:
        stopfiltered = [str(x) for x in wl if x not in stop]
print(stopfiltered)
