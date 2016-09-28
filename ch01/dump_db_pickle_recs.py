#!/bin/env python
# -*- coding: utf-8 -*-

import pickle
import glob

for filename in glob.glob('*pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)
    
