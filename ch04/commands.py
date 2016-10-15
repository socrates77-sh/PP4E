#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

from sys import argv
import sys
sys.path.append(r'e:\py\PP4E\ch04')
from scanfile import scanner


class UnknownCommand(Exception):
    pass


def processLine(line):
    if line[0] == '*':
        print('Ms.', line[1:-1])
    elif line[0] == '+':
        print('Mr.', line[1:-1])
    else:
        raise UnknownCommand(line)


filename = 'data.txt'
if len(argv) == 2:
    filename = argv[1]
scanner(filename, processLine)
