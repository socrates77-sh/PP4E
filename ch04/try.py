#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import os
import sys

os.chdir('e:\py\PP4E\ch04')

for (dirname, subshere, fileshere) in os.walk('.'):
    print('[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname))
    # for l in subshere:
    #     print(l)
    print(len(dirname))
    print(len(subshere))
    print(len(fileshere))
    print()

