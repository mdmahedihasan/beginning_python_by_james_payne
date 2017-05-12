import os
import os.path
import re
from stat import *


def find(where=".*", content=None, start=".", ext=None, logic=None):
    context = {}
    context['where'] = where
    context['content'] = content
    context['return'] = []

    os.walk(start, find_file, context)

    return context['return']


def find_file(context, dir, files):
    for file in files:
        path = os.path.join(dir, file)
        path = os.path.normcase(path)
        try:
            ext = os.path.splitext(file)[1][1:]
        except:
            ext = ''
        stat = os.stat(path)
        size = stat[ST_SIZE]

        # Do not treat directories like files.
        if S_ISDIR(stat[ST_MODE]):
            continue

        # Do filtration based on the original parameters of find()
        if not re.search(context['where'], file):
            continue

        # Do content filtration last, to avoid it as much as possible
        if context['content']:
            f = open(path, 'r')
            match = 0
            for l in f.readlines():
                if re.search(context['content'], l):
                    match = 1
                    break
            f.close()
            if not match:
                continue

    # Build the return value for any files that passed the filtration tests.
        file_return = (path, file, ext, size)
        context['return'].append(file_return)
