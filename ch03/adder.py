#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys

sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)
print(sum)
