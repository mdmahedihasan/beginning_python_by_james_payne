import os, sys

if sys.platform == 'win32':
    print("Running on a windows platform")
    command = "cmd.exe"

if sys.platform == 'linux2':
    print("Running linux")
    command = "uname -a"

os.system(command)
