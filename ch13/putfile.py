"""
Store an arbitrary file by FTP in binary mode.  Uses anonymous
ftp unless you pass in a user=(name, pswd) tuple of arguments.
"""

import ftplib                    # socket-based FTP tools


def putfile(file, site, dir, user=(), *, verbose=True):
    """
    store a file by ftp to a site/directory
    anonymous or real login, binary transfer
    """
    if verbose:
        print('Uploading', file)
    local = open(file, 'rb')               # local file of same name
    remote = ftplib.FTP()               # connect to FTP site
    remote.connect(site, 2121)
    remote.login(*user)                     # anonymous or real login
    remote.cwd(dir)
    remote.storbinary('STOR ' + file, local, 1024)
    remote.quit()
    local.close()
    if verbose:
        print('Upload done.')


if __name__ == '__main__':
    site = '192.168.137.118'
    dir = '.'
    import sys
    import getpass
    # filename on cmdline
    # pswd = getpass.getpass(site + ' pswd?')
    putfile(sys.argv[1], site, dir, user=())
