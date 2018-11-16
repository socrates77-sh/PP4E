#!/usr/local/bin/python
"""
A Python script to download and play a media file by FTP.
Uses getfile.py, a utility module which encapsulates FTP step.
"""

import getfile
from getpass import getpass
filename = 'IMG_20150803_173117.jpg'

# fetch with utility
getfile.getfile(file=filename,
                site='192.168.137.118',
                dir='./DCIM/Camera',
                user=(),
                refetch=True)

# rest is the same
if input('Open file?') in ['Y', 'y']:
    from playfile import playfile
    playfile(filename)
