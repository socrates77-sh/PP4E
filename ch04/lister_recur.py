#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys
import os


def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):  # list files here
        path = os.path.join(currdir, file)  # add dir path back
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)  # recur into subdirs


if __name__ == '__main__':
    mylister(sys.argv[1])  # dir name in cmdline
