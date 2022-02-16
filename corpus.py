# module for stopwords, lemmatize

stoplist = []
lemmalist = []

def stopwords(chlang):
    if chlang == "russian":
        with open("stopwordsru.txt", "r") as file:
            stoplist = file.read().split("\n")
    return stoplist

def lemmatize(chlang):
    if chlang == "russian":
        with open("lemmatizer.txt", "r") as file:
            for line in file:
                if not line:
                    continue
                else:
                    left, right = line.split(" ")
                    lemmalist[left] = right
    return lemmadict
