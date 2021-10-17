import os

basepath = os.getcwd()
path = (basepath + "/.vscode/python_course/1DV501")
print(path)


def print_subdirectories(dir_path):
    entries = os.scandir(dir_path)
    for dir in entries:
        if dir.is_dir():
            print(dir)
            print_subdirectories(dir)


print_subdirectories(path)
