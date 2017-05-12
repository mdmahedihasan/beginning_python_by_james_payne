import os, sys

if sys.platform == 'win32':
    print("Running on a windows platform")
    command = "C:\\Windows\\System32\\cmd.exe"
    params = []

if sys.platform == 'linux2':
    print("Running on a linux system, identified by %s " % sys.platform)
    command = '/bin/uname'
    params = ['uname', '-a']

print("Running %s" % command)
os.spawnv(os.P_WAIT, command, params)
