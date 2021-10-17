import os

basepath = os.getcwd()
path = (basepath + "/.vscode/python_course/1DV501")
print(path)


def pretty_print_subdirectories(dir_path, n=0):
    entries = os.scandir(dir_path)
    lst = os.listdir(dir_path)
    i = 0
    for dir in entries:
        if dir.is_dir():
            print("\t" * n, lst[i])
            pretty_print_subdirectories(dir, n + 1)
        i += 1


pretty_print_subdirectories(path)
