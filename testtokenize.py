from sentences import Sentences
from words import Words
from punctuation import Punctuation
import corpus

xlist = []

# to awoid some problems with not good writting text
# для избежания возможной ошибки при неправильном форматировании данных
with open("data.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            xlist.append(row)
        varstring = " ".join(xlist)

#tokenize string to words
w = Words(varstring)
wl = w.load()
print(wl)

# load stop words
stop = corpus.stopwords("russian")
for i in wl:
        stopfiltered = [str(x) for x in wl if x not in stop]
print(stopfiltered)
