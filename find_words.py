import os

basepath = os.getcwd()
pathfA = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/holy_grail.txt")
pathfB = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/._eng_news_100K-sentences.txt")
pathT = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/find_words_test.txt")
pathW = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/for_writing.txt")


def read_file(path):
    s = ""
    lst = []
    ret = []
    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            s += line
        lst = s.split()
        for i in lst:
            ret.append(clean(i))
    return ret


def clean(s):
    ret = ""
    for i in range(0, len(s)):
        if (ord(s[i]) > 64 and ord(s[i]) < 91) or \
             (ord(s[i]) > 96 and ord(s[i]) < 123):
            ret += s[i]
        ret = ret.lower()
    return ret


def write_file(path, words):
    sz = 0
    with open(path, "w", encoding='utf-8') as file:
        for i in words:
            file.write(i)
            file.write(" ")
            sz += len(i)
            if sz > 100:
                file.write('\n')
                sz = 0


write_file(pathW, read_file(pathfA))
