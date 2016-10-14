#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys

lines = sys.stdin.readlines()
lines.sort()
for lines in lines:
    print(lines, end='')
