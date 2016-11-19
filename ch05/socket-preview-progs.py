#!/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'socrates'

import sys

sys.path.append("ch05")
from socket_preview import server, client  # both use same port number
import sys, os
from threading import Thread

mode = int(sys.argv[1])
if mode == 1:  # run server in this process
    server()
elif mode == 2:  # run client in this process
    client('client:process=%s' % os.getpid())
else:  # run 5 client threads in process
    for i in range(5):
        Thread(target=client, args=('client:thread=%s' % i,)).start()