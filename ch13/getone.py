#!/usr/local/bin/python
"""
A Python script to download and play a media file by FTP.  Uses ftplib, the ftp 
protocol handler which uses sockets.  Ftp runs on 2 sockets (one for data, one 
for control--on ports 20 and 21) and imposes message text formats, but Python's
ftplib module hides most of this protocol's details.  Change for your site/file.
"""

import os
import sys
from getpass import getpass                   # hidden password input
from ftplib import FTP                        # socket-based FTP tools

nonpassive = False                           # force active mode FTP for server?
filename = 'IMG_20150803_173117.jpg'                   # file to be downloaded
dirname = './DCIM/Camera'                             # remote directory to fetch from
sitename = '192.168.137.86'                   # FTP site to contact
# userinfo = ('lutz', getpass('Pswd?'))      # use () for anonymous
if len(sys.argv) > 1:
    filename = sys.argv[1]  # filename on command line?

print('Connecting...')
connection = FTP()                  # connect to FTP site
connection.connect(sitename, 2121)
# connection.login(*userinfo)                 # default is anonymous login
connection.login()                 # default is anonymous login
connection.cwd(dirname)                     # xfer 1k at a time to localfile
if nonpassive:                              # force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')            # local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

if input('Open file?') in ['Y', 'y']:
    from playfile import playfile
    playfile(filename)
