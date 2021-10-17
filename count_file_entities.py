import os

basepath = os.getcwd()
path = (basepath + "/.vscode/python_course/1DV501/hs223nr_assign2")


def count_directories(dir_path):
    return len(os.listdir(dir_path))


def count_py_files(dir_path):
    lst = os.listdir(dir_path)
    ret = 0
    for s in lst:
        if s.endswith('.py'):
            ret += 1
    return ret


print("Dir Count:", count_directories(path))
print("Py-file Count:", count_py_files(path))
