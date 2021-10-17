import os

basepath = os.getcwd()
pathfA = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/holy_grail.txt")
pathfB = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/eng_news_100K-sentences.txt")
pathT = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/find_words_test.txt")
pathW = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/for_writing.txt")


def read_file(path):
    s = ""
    lst = []
    ret = ""
    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            s += line
        lst = s.split()
        for i in lst:
            ret += clean(i)
    return ret.split()


def clean(s):
    ret = ""
    for i in range(0, len(s)):
        if (ord(s[i]) > 64 and ord(s[i]) < 91) or \
             (ord(s[i]) > 96 and ord(s[i]) < 123):
            ret += s[i] + " "
        ret = ret.lower()
    return ret


def toDict(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = "*"
        dct[i] += "*"
    return dct


def get_key(tpl):
    return tpl[0]


def prettyPrint(dct):
    items = list(dct.items())
    value_sorted = sorted(items, key=get_key)
    for i in value_sorted:
        print(i[0], "|", i[1], "\n")


prettyPrint(toDict(read_file(pathfA)))
