"""
test effect of connecting standard streams to text and binary mode files
same holds true for socket.makefile: print requires text mode, but text
mode precludes unbuffered mode -- use -u or sys.stdout.flush() calls
"""

import sys


def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp

reader(open('test-stream-modes.py'))         # works: input() returns text
reader(open('test-stream-modes.py', 'rb'))   # works: but input() returns bytes


def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp

# works: print() passes text str to .write()
writer(open('temp', 'w'))
print(open('temp').read())

# FAILS on print: binary mode requires bytes
writer(open('temp', 'wb'))
writer(open('temp', 'w', 0))          # FAILS on open: text must be unbuffered
