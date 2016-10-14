#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

print('Got this: "%s"' % input())
import sys

data = sys.stdin.readline()[:-1]
print('The meaning of life is', data, int(data) * 2)
