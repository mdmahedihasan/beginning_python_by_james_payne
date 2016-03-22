import os


def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print(full_path)
        if os.path.isdir(full_path):
            print_tree(full_path)


print(print_tree("D:\FALSE\workspace\Python_Workspace\Beginning Python_James Payne"))
