#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import threading, sys, time


def action():
    sys.exit()  # or raise SystemExit()
    print('not reached')


threading.Thread(target=action).start()
time.sleep(2)
print('Main exit')