import time
import os

mod_time = os.path.getmtime("C:\\Python35-32")
print(time.ctime(mod_time))
