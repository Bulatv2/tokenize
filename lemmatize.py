#class Lemmatize

lemmalist = []
llist = []
rlist = []

with open("lemmas.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right)
class Lemmatize:
    def __init__(self, text):
        self.text = text
    def load(self):
        for i in range(len(llist)):
            for j in self.text:
                if i == j:
                    lemmalist.append(rlist[i])
                else:
                    lemmalist.append(j)
            return lemmalist
