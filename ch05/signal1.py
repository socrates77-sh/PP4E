#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys, signal, time


def now(): return time.ctime(time.time())  # current time string


def onSignal(signum, stackframe):  # python signal handler
    print('Got signal', signum, 'at', now())  # most handlers stay in effect


signum = int(sys.argv[1])
signal.signal(signum, onSignal)  # install signal handler
while True: signal.pause()  # wait for signals (or: pass)