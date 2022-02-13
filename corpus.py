# module for stopwords, lemmatize, stemming

stoplist = []
lemmadict = []
stemdict = {}

def stopwords(chlang):
    if chlang == "russian":
        with open("stopwordsru.txt", "r") as file:
            stoplist = file.read().split("\n")
    return stoplist

def lemma(chlang):
    if chlang == "russian":
        with open("lemmas.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                else:
                    left, right = line.split(":")
                    lemmadict[left] = right
    return lemmadict

def stem(chlang):
    if chlang == "russian":
        with open("stems.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                else:
                    left, right = line.split(":")
                    stemdict[left] = right
    return stemdict
