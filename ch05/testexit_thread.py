#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import _thread as thread

exitstat = 0


def child():
    global exitstat  # process global names
    exitstat += 1  # shared by all threads
    threadid = thread.get_ident()
    print('Hello from child', threadid, exitstat)
    thread.exit()
    print('never reached')


def parent():
    while True:
        thread.start_new_thread(child, ())
        if input() == 'q': break


if __name__ == '__main__': parent()
