import os
import math as m

basepath = os.getcwd()
pathFA = (basepath + "/.vscode/python_course/1DV501/hs223nr_assign3\
/test/file_10000integers_A.txt")
pathFB = (basepath + "/.vscode/python_course/1DV501/hs223nr_assign3\
/test/file_10000integers_B.txt")


def read_integers1(path):
    s = ""
    lst = []
    with open(path, "r") as file:
        for line in file:
            s += line.replace(',', ' ')
        lst = s.split()
    lst = [float(x) for x in lst]  # from finxter.com
    return lst


def read_integers2(path):
    s = ""
    lst = []
    with open(path, "r") as file:
        for line in file:
            s += line.replace(':', ' ')
        lst = s.split()
    lst = [float(x) for x in lst]  # from finxter.com
    return lst


def mean(lst):
    tot = 0.0
    for i in lst:
        tot += i
    return tot / len(lst)


def std(lst):
    men = mean(lst)
    retlst = []
    for i in lst:
        retlst.append((i - men) ** 2)
    return m.sqrt(mean(retlst))


mA = mean(read_integers1(pathFA))
mB = mean(read_integers2(pathFB))
stdA = std((read_integers1(pathFA)))
stdB = std((read_integers2(pathFB)))

print(mA, stdA)
print(mB, stdB)
