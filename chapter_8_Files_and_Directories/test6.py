import os


def print_dir(dir_path):
    for name in os.listdir(dir_path):
        print(os.path.join(dir_path, name))


print_dir("C:\\Python35-32")
