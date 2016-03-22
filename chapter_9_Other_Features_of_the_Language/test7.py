import os

pid = os.fork()
if pid == 0:
    print("This is the child")
else:
    print("The child is pid %d " % pid)
