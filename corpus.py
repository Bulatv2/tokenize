# module stopwords

xlist = []
def stopwords(chlang):
    if chlang == "russian":
        with open("stopwordsru.txt", "r") as file:
            xlist = file.read().split("\n")
    return xlist

__version__ = "0.1"
