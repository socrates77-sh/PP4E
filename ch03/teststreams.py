#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'


def interact():
    print('Hello steam world')
    while True:
        try:
            reply = input('Enter a number>')
        except EOFError:
            break
        else:
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()