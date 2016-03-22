import os

pid = os.fork()
print("second test")
if pid == 0:
    print("This is the child")
    print("I'm going to exec another program now")
    os.execl('bin/cat', 'cat', 'etc/motd')
else:
    print("The child is pid %d" % pid)
    os.wait()
