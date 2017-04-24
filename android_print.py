# -*- coding:utf-8 -*-

import sys

def printinfo(printinfo):
    getfilesystemencoding = sys.getfilesystemencoding()
    if isinstance(printinfo, file):
        readlines = printinfo.readlines()
        for line in readlines:
            print line.decode("utf-8").encode(getfilesystemencoding)
    if isinstance(printinfo, str):
        print printinfo.decode("utf-8").encode(getfilesystemencoding)

