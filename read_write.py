import os

basepath = os.getcwd()
path = (basepath + "/.vscode/python_course/1DV501/hs223nr_assign3\
/test/testForReadWrite.txt")
print(path)


def read_file(fpath):
    file = open(fpath, "r")
    s = ""
    for line in file:
        print(line)
        s += line
    file.close()
    return s


def write_file(lines, fpath):
    file = open(fpath, "w")
    file.write(lines)
    file.close()


write_file(read_file(path), path)
