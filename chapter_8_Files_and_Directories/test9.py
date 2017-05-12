import os
import time


def print_dir_info(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        file_size = os.path.getsize(full_path)
        mod_time = time.ctime(os.path.getmtime(full_path))
        print("%-32s: %8d bytes,  modified at-  %s " % (name, file_size,mod_time))


print(
print_dir_info("D:\FALSE\workspace\Python_Workspace\Beginning Python_James Payne\chapter_8_Files_and_Directories"))
