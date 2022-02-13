# module to count vector

from words import Words

def vector(getlist):
    klist = []
    vlist = []
    nlist = []
    varstring = " ".join(getlist)
    instvect = Words(varstring)
    instv = instvect.load()
    for i in getlist:
        insth = Words(i)
        w = insth.load()
        nlist.append(w)
    for i in range(len(nlist)):
        klist.append([0]*len(instv))
    for k in instv:
        for i in nlist:
            for j in i:
                if k == j:
                    klist[nlist.index(i)][instv.index(k)] = 1
    return klist
"""
def getdata(xarg):
    count = 0
    count2 = 0
    answ = ""
    nlist = []
    listvect = []
    listvect2 = []
    rlist = []
    word = Words(xarg)
    w = word.load()
    for k in w:
        for i, x in enumerate(vector.bow()):
            if x == k:
                nlist.append(i)

    for j in vector.vector():
        count = 0
        for i in nlist:
            if j[i] != 0:
                count += 1
        count2 += 1
        if count != 0:
            listvect.append(count)
            listvect2.append(count2-1)

    for i in listvect:
        y = i/len(nlist)
        rlist.append(y)

    if len(rlist) == 1:
        for i in listvect2:
            answ = slist[i]
    else:
        for i in rlist:
            if i == max(rlist):
                m = rlist.index(i)
                v = listvect2[m]
                answ = slist[v]
    
    return answ
"""
