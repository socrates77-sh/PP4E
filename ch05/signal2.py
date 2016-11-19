#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys, signal, time


def now(): return time.asctime()


def onSignal(signum, stackframe):  # python signal handler
    print('Got alarm', signum, 'at', now())  # most handlers stay in effect


while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, onSignal)  # install signal handler
    signal.alarm(5)  # do signal in 5 seconds
    signal.pause()  # wait for signals