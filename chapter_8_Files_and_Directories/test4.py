import os.path

print(os.path.join("books", "python"))

parent_path, name = os.path.split(
    "D:\FALSE\workspace\Python_Workspace\Beginning Python_James Payne\chapter_8_Files_and_Directories")
print(parent_path)
print(name)