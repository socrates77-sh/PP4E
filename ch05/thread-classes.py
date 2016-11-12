import threading


class Mythread(threading.Thread):  # subclass Thread object
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count  # per-thread state information
        self.mutex = mutex  # shared objects, not globals
        threading.Thread.__init__(self)

    def run(self):  # run provides thread logic
        for i in range(self.count):  # still sync stdout access
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))


stdoutmutex = threading.Lock()  # same as thread.allocate_lock()
threads = []
for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)  # make/start 10 threads
    thread.start()  # starts run method in a thread
    threads.append(thread)
for thread in threads:
    thread.join()  # wait for thread exits
print('Main thread exiting.')