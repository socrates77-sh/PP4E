# output line buffered (unbuffered) if stdout is a terminal, buffered by default for
# other devices: use -u or sys.stdout.flush() to avoid delayed output on
# pipe/socket

import time
import sys
for i in range(5):
    # print transfers per stream buffering
    print(time.asctime())
    sys.stdout.write('spam\n')            # ditto for direct stream file access
    # unles sys.stdout reset to other file
    time.sleep(2)
