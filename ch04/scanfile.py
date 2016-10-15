#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'


def scanner(name, function):
    for line in open(name,'r'):
        function(line)
