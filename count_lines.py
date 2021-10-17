import os

basepath = os.getcwd()
basepath = (basepath + "/.vscode/python_course/1DV501/")


def getPyLines(dir_path, tab=0):
    entries = os.scandir(dir_path)
    lst = os.listdir(dir_path)
    i = 0
    numLines = 0
    for e in entries:
        x = str(e)
        if e.is_dir():
            print("\t" * tab, lst[i])
            numLines += getPyLines(e, tab + 1)
        elif str(e).endswith('py', len(x) - 4, len(x) - 2):
            numLines += getNumPyLines(e)
            print("\t" * (tab + 1), lst[i], getNumPyLines(e))
        i += 1
    return numLines


def getNumPyLines(fpath):
    ret = 0
    with open(fpath, "r") as file:
        for line in file:
            if line != "\n":
                ret += 1
    return ret


print("Python Line Count:", getPyLines(basepath))
