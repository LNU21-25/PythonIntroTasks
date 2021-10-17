import os

basepath = os.getcwd()
pathFA = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/file_10000integers_A.txt")
pathFB = (basepath + "/python_course/1DV501/hs223nr_assign3\
/test/file_10000integers_B.txt")


def count_different(lst):
    st = set(lst)
    return len(st)


def count_occurances(lst):
    dct = {}
    for i in lst:
        if i not in dct:
            dct[i] = 0
        dct[i] += 1
    return dct


def read_integers1(path):
    s = ""
    lst = []
    with open(path, "r") as file:
        for line in file:
            s += line.replace(',', ' ')
        lst = s.split()
    return lst


def read_integers2(path):
    s = ""
    lst = []
    with open(path, "r") as file:
        for line in file:
            s += line.replace(':', ' ')
        lst = s.split()
    return lst


def get_value(tpl):
    return tpl[1]


def getFive(dct):
    items = list(dct.items())
    value_sorted = sorted(items, key=get_value)
    return value_sorted[(len(value_sorted)-5): len(value_sorted)]


print("Number of different integers in file_10000integers_A.\
txt:", count_different(read_integers1(pathFA)))
print("Number of different integers in file_10000integers_B.\
txt:", count_different(read_integers2(pathFB)))
print("Top 5 repeated numbers in file_10000integers_A.\
txt:", getFive(count_occurances(read_integers1(pathFA))))
print("Top 5 repeated numbers in file_10000integers_B.\
txt:", getFive(count_occurances(read_integers2(pathFB))))
