import os, os.path
import re


def print_pdf(arg, dir, files):
    for file in files:
        path = os.path.join(dir, file)
        path = os.path.normcase(path)
        if not re.search(r".*\.pdf", path):
            continue
        if re.search(r".\.hu", path):
            continue
        print(path)

for arg, dir, files in os.walk('.'):
    pass
