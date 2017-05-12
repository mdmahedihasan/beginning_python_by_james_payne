import os


def split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return (parent_path,)

    else:
        return split_fully(parent_path) + (name,)


print(split_fully("D:\FALSE\workspace\Python_Workspace\Beginning Python_James Payne\chapter_8_Files_and_Directories"))

print(os.path.splitext("image.jpg"))
